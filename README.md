# **Medical Transcription Data Extraction**

## **Overview**
Medical professionals often summarize patient encounters in transcripts written in natural language, which include details about symptoms, diagnoses, and treatments. These transcripts are essential for:
- Medical documentation.
- Insurance processing.
- Billing purposes (e.g., with ICD-10 codes).

Extracting this data accurately can be challenging due to the dense and unstructured nature of the transcripts.

At **Lakeside Healthcare Network**, we aim to:
1. Automatically extract key medical information from transcripts using **OpenAI's API**.
2. Match the extracted treatments with the corresponding **ICD-10 codes** for standardized documentation.

---

## **Dataset**

### **File**: `transcriptions.csv`

The dataset consists of anonymized medical transcriptions organized by specialty.

| **Column**            | **Description**                                                                 |
|------------------------|---------------------------------------------------------------------------------|
| `medical_specialty`    | The medical specialty associated with each transcription.                      |
| `transcription`        | Detailed medical transcription texts, with insights into the medical case.     |

---

## **Project Goals**

1. **Data Extraction**:
   - Extract the following fields from each transcription:
     - **Age**: The patient's age (if mentioned).
     - **Medical Specialty**: The associated medical specialty (e.g., Cardiology, Orthopedics).
     - **Recommended Treatment**: Suggested treatments, procedures, or prescriptions.
   
2. **ICD-10 Code Matching**:
   - Map each extracted **Recommended Treatment** to its corresponding **ICD-10 code**.

3. **Structured Data Output**:
   - Save the extracted information in a structured format using **pandas**.

---

## **Approach**

1. **Leverage OpenAI API**:
   - Use OpenAI models to:
     - Extract relevant information from unstructured text.
     - Identify and standardize medical terminology.
     - Map treatments to ICD-10 codes.

2. **Automate the Workflow**:
   - Automatically process transcripts and generate structured output.

---

## **Expected Output**

### **Sample Extracted Fields**

| **Age** | **Medical Specialty**       | **Recommended Treatment**                                   | **ICD-10 Code**    |
|---------|-----------------------------|------------------------------------------------------------|--------------------|
| 35      | Cardiology                  | Lifestyle modification and atorvastatin prescription.      | E78.0 (Hyperlipidemia) |
| 22      | Orthopedics                 | ACL reconstruction surgery.                                | S83.511A (ACL Tear) |
| 45      | Pulmonology                 | Prescribed albuterol inhaler for asthma management.        | J45.909 (Asthma)   |

---

## **Screenshots**

### **Transcription Dataset**

![Transcription Dataset Overview](images/Screenshot%202024-12-07%20203332.png)

### **Sample Output**

![Sample Output Structure](images/Screenshot%202024-12-07%20203348.png)

---

## **Implementation**

1. **Data Input**:
   - Load the `transcriptions.csv` file containing the dataset.

2. **API Integration**:
   - Use the **OpenAI API** to extract `Age`, `Medical Specialty`, and `Recommended Treatment` from each transcription.

3. **ICD-10 Code Mapping**:
   - Match the extracted treatments with their corresponding **ICD-10 codes**.

4. **Output DataFrame**:
   - Store the structured output in a pandas DataFrame named `df_structured`.

5. **Save Results**:
   - Export the DataFrame to a `.csv` file for further analysis.

---

## **Next Steps**

- Automate the pipeline to process new transcription files.
- Expand the mapping database to cover additional specialties and ICD-10 codes.
- Implement validation checks for better accuracy.

---

## **Credits**
- **API**: Powered by [OpenAI](https://openai.com/).
- **ICD-10 Codes**: Retrieved from the official [ICD-10 database](https://www.who.int/standards/classifications/classification-of-diseases).

---
