import streamlit as st
import pandas as pd
import nltk
from app import analyze_multiple_resumes, download_nltk_resources
import io  # For handling in-memory file objects

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
            
            # Store results in a Pandas DataFrame for CSV export
            resume_data = []
            for resume_name, scores in results.items():
                if 'error' in scores:
                    resume_data.append({
                        "Resume": resume_name,
                        "Error": scores['error']
                    })
                else:
                    resume_data.append({
                        "Resume": resume_name,
                        "Final Score": scores['final_score'],
                        "Keyword Match Score": scores['keyword_score'],
                        "Resume Structure Score": scores['structure_score'],
                        "Skill Match Score": scores['skill_match_score'],
                        "Years of Experience": scores['experience_years'],
                        "Contact Info": scores['contact_info']
                    })

            # Create DataFrame
            df = pd.DataFrame(resume_data)

            # Display results
            st.subheader("Resume Scores:")
            st.write(df)

            # CSV Download Button
            csv = df.to_csv(index=False)
            st.download_button(
                label="Download Resume Scores as CSV",
                data=csv,
                file_name="resume_scores.csv",
                mime="text/csv",
            )
        
        except Exception as e:
            st.error(f"An error occurred while processing the resumes: {str(e)}")
    else:
        st.error("Please fill in all fields and upload at least one resume.")
