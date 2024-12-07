import json
import pandas as pd
import os
import openai
import streamlit as st

os.environ["OPENAI_API_KEY"] = "api-key"
openai.api_key = os.environ["OPENAI_API_KEY"]

st.set_page_config(
    page_title="Medical Transcription Analyzer",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

with st.sidebar:
    st.image("https://via.placeholder.com/300x100?text=MedAI+Analyzer", use_column_width=True)
    st.title("Navigation")
    st.markdown(
        """
        **Options**:
        - Upload transcriptions for analysis
        - Extract Age and Treatment
        - Fetch ICD codes
        """
    )
    st.markdown("👨‍⚕️ Built for healthcare professionals.")

st.title("🩺 Medical Transcription Analyzer")
st.markdown(
    """
    A tool to **transcribe**, **analyze**, and **structure** medical data using **OpenAI's GPT API**.
    """
)

st.markdown("### Steps:")
st.write(
    """
    1. Upload your **CSV file** containing medical transcriptions.
    2. Extract information such as **Age** and **Recommended Treatment/Procedure**.
    3. Fetch **ICD Codes** for the recommended treatments.
    4. Download the **processed structured data** as a CSV file.
    """
)

uploaded_file = st.file_uploader(
    "📂 Upload a CSV file containing medical transcriptions", type="csv"
)

def extract_info_with_openai(transcription):
    """Extracts age and recommended treatment or procedure from a transcription using OpenAI."""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "Extract the patient's age (in years) and the recommended treatment or procedure "
                    "from the provided medical transcription. If either detail is missing, respond with "
                    "'Age: Not Found' or 'Recommended Treatment/Procedure: Not Found'. Return the result "
                    "as a JSON object like this: {'Age': <age>, 'Recommended Treatment/Procedure': <treatment>}."
                ),
            },
            {
                "role": "user",
                "content": f"Transcription: {transcription}",
            },
        ],
        temperature=0.3,
    )
    content = response['choices'][0]['message']['content']
    
    try:
        extracted_data = json.loads(content.replace("'", '"'))
    except json.JSONDecodeError:
        extracted_data = {"Age": "Not Found", "Recommended Treatment/Procedure": "Not Found"}

    return extracted_data


def get_icd_codes(treatment):
    """Retrieves ICD codes for a given treatment using OpenAI."""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a medical assistant knowledgeable about ICD codes.",
            },
            {
                "role": "user",
                "content": f"Provide the ICD codes for the following treatment or procedure: {treatment}.",
            },
        ],
        temperature=0.3,
    )
    return response['choices'][0]['message']['content']

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.markdown("### Uploaded Data Preview")
    st.dataframe(df.head(), use_container_width=True)

    processed_data = []

    with st.spinner("🔍 Processing transcriptions..."):
        for _, row in df.iterrows():
            transcription = row["transcription"]
            medical_specialty = row["medical_specialty"]

            extracted_data = extract_info_with_openai(transcription)
            treatment = extracted_data.get("Recommended Treatment/Procedure", "Not Found")

            if treatment != "Not Found":
                icd_code = get_icd_codes(treatment)
            else:
                icd_code = "Not Found"

            structured_record = {
                "Age": extracted_data.get("Age", "Not Found"),
                "Recommended Treatment/Procedure": treatment,
                "Medical Specialty": medical_specialty,
                "ICD Code": icd_code,
            }
            processed_data.append(structured_record)

    df_structured = pd.DataFrame(processed_data)

    st.markdown("### Processed Data")
    st.dataframe(df_structured, use_container_width=True)

    csv = df_structured.to_csv(index=False)
    st.download_button(
        label="⬇️ Download Processed Data as CSV",
        data=csv,
        file_name="structured_transcriptions.csv",
        mime="text/csv",
    )

st.markdown("---")
st.markdown(
    """
    **Medical Transcription Analyzer**: Built with ❤️ using [Streamlit](https://streamlit.io/) and [OpenAI](https://openai.com/).
    """
)
