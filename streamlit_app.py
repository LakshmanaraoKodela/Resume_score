import streamlit as st
import io
import xlsxwriter
from app import analyze_multiple_resumes, download_nltk_resources

# Set page configuration
st.set_page_config(page_title="ATS Resume Analyzer", layout="wide")

# Title
st.markdown('<h1 style="text-align: center; color: #4CAF50;">ATS Score Analyzer!</h1>', unsafe_allow_html=True)

# Download NLTK resources at the start of the app
with st.spinner('Initializing NLTK resources...'):
    download_nltk_resources()

# Job Description input
job_description = st.text_area("Enter Job Description", height=300)
if job_description:
    st.subheader("Job Description Preview:")
    st.write(job_description)

# Skills input
skills = st.text_input("Enter Skills (comma-separated)")
if skills:
    skills = [skill.strip() for skill in skills.split(",")]
    st.subheader("Skills Preview:")
    st.write(", ".join(skills))

# Experience input
experience_years = st.number_input("Enter Required Experience (in years)", min_value=0)

# File upload
uploaded_files = st.file_uploader("Upload Resumes", type=["pdf", "docx"], accept_multiple_files=True)

if st.button("View Scores"):
    if job_description and skills and experience_years > 0 and uploaded_files:
        resume_paths = []
        for uploaded_file in uploaded_files:
            with open(uploaded_file.name, "wb") as f:
                f.write(uploaded_file.getbuffer())
                resume_paths.append(uploaded_file.name)
        
        try:
            # Analyze resumes
            results = analyze_multiple_resumes(resume_paths, job_description, skills, experience_years)

            # Create an Excel file in memory
            output = io.BytesIO()
            workbook = xlsxwriter.Workbook(output, {'in_memory': True})
            worksheet = workbook.add_worksheet()

            # Write headers
            worksheet.write_row(0, 0, ['Resume Name', 'Final Score', 'Keyword Match Score', 'Resume Structure Score', 'Skill Match Score', 'Years of Experience', 'Contact Info'])

            # Write data
            row = 1
            for resume_name, scores in results.items():
                if 'error' in scores:
                    worksheet.write_row(row, 0, [resume_name, scores['error'], '', '', '', '', ''])
                else:
                    worksheet.write_row(row, 0, [resume_name, scores['final_score'], scores['keyword_score'], scores['structure_score'], scores['skill_match_score'], scores['experience_years'], scores['contact_info']])
                row += 1

            # Close the workbook and prepare data for download
            workbook.close()
            output.seek(0)

            # Create download button for Excel
            st.download_button(
                label="Download results as Excel",
                data=output,
                file_name='resume_scores.xlsx',
                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )

        except Exception as e:
            st.error(f"An error occurred while processing the resumes: {str(e)}")
    else:
        st.error("Please fill in all fields and upload at least one resume.")
