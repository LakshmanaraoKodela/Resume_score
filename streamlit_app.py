# import streamlit as st
# import nltk
# from app import analyze_multiple_resumes, download_nltk_resources

# # Set page configuration
# st.set_page_config(page_title="ATS Resume Analyzer", layout="wide")

# # Title
# st.markdown('<h1 style="text-align: center; color: #4CAF50;">ATS Score Analyzer!</h1>', unsafe_allow_html=True)

# # Download NLTK resources at the start of the app
# with st.spinner('Initializing NLTK resources...'):
#     download_nltk_resources()
# # st.success.subheader('Ats Score Analyzer!')

# # Job Description input
# job_description = st.text_area("Enter Job Description", height=300)
# if job_description:
#     st.subheader("Job Description Preview:")
#     st.write(job_description)

# # Skills input
# skills = st.text_input("Enter Skills (comma-separated)")
# if skills:
#     skills = [skill.strip() for skill in skills.split(",")]
#     st.subheader("Skills Preview:")
#     st.write(", ".join(skills))

# # Experience input
# experience_years = st.number_input("Enter Required Experience (in years)", min_value=0)

# # File upload
# uploaded_files = st.file_uploader("Upload Resumes", type=["pdf", "docx"], accept_multiple_files=True)

# if st.button("View Scores"):
#     if job_description and skills and experience_years > 0 and uploaded_files:
#         resume_paths = []
#         for uploaded_file in uploaded_files:
#             with open(uploaded_file.name, "wb") as f:
#                 f.write(uploaded_file.getbuffer())
#                 resume_paths.append(uploaded_file.name)
        
#         try:
#             results = analyze_multiple_resumes(resume_paths, job_description, skills, experience_years)
        
#             st.subheader("Resume Scores:")
#             for resume_name, scores in results.items():
#                 st.write(f"### {resume_name}")
#                 if 'error' in scores:
#                     st.error(f"Error processing this resume: {scores['error']}")
#                 else:
#                     st.write(f"**Final Score:** {scores['final_score']:.2f}")
#                     st.write(f"**Keyword Match Score:** {scores['keyword_score']:.2f}")
#                     st.write(f"**Resume Structure Score:** {scores['structure_score']:.2f}")
#                     st.write(f"**Skill Match Score:** {scores['skill_match_score']:.2f}")
#                     st.write(f"**Years of Experience:** {scores['experience_years']}")
#                     st.write(f"**Contact Info:** {scores['contact_info']}")
#                 st.write("---")
#         except Exception as e:
#             st.error(f"An error occurred while processing the resumes: {str(e)}")
#     else:
#         st.error("Please fill in all fields and upload at least one resume.")


import streamlit as st
import nltk
import pandas as pd
from app import analyze_multiple_resumes, download_nltk_resources

# Function to save data to CSV
def save_to_csv(job_description, skills, experience_years, resume_names):
    data = {
        "Job Description": [job_description],
        "Skills": [", ".join(skills)],
        "Experience Years": [experience_years],
        "Resume Names": [", ".join(resume_names)]
    }
    df = pd.DataFrame(data)
    df.to_csv("submitted_data.csv", mode='a', header=not pd.io.common.file_exists("submitted_data.csv"), index=False)

# Set page configuration
st.set_page_config(page_title="ATS Resume Analyzer", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    /* Your CSS styles here */
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 style="text-align: center; color: #4CAF50;">ATS Score Analyzer!</h1>', unsafe_allow_html=True)

# Download NLTK resources at the start of the app
with st.spinner('Initializing NLTK resources...'):
    download_nltk_resources()
st.success('NLTK resources initialized successfully!')

# Job Description input
job_description = st.text_area("Enter Job Description", height=300)
if job_description:
    st.subheader("Job Description Preview:")
    st.markdown(f'<div class="preview">{job_description}</div>', unsafe_allow_html=True)

# Skills input
skills = st.text_input("Enter Skills (comma-separated)")
if skills:
    skills = [skill.strip() for skill in skills.split(",")]
    st.subheader("Skills Preview:")
    st.markdown(f'<div class="preview">{", ".join(skills)}</div>', unsafe_allow_html=True)

# Experience input
experience_years = st.number_input("Enter Required Experience (in years)", min_value=0)

# File upload
uploaded_files = st.file_uploader("Upload Resumes", type=["pdf", "docx"], accept_multiple_files=True)

if st.button("View Scores", key="view_scores", help="Click to analyze the uploaded resumes"):
    if job_description and skills and experience_years > 0 and uploaded_files:
        resume_names = [uploaded_file.name for uploaded_file in uploaded_files]
        
        resume_paths = []
        for uploaded_file in uploaded_files:
            with open(uploaded_file.name, "wb") as f:
                f.write(uploaded_file.getbuffer())
                resume_paths.append(uploaded_file.name)
        
        try:
            results = analyze_multiple_resumes(resume_paths, job_description, skills, experience_years)
            save_to_csv(job_description, skills, experience_years, resume_names)  # Save data to CSV
        
            st.subheader("Resume Scores:")
            for resume_name, scores in results.items():
                with st.expander(resume_name):
                    if 'error' in scores:
                        st.error(f"Error processing this resume: {scores['error']}", icon="🚨")
                    else:
                        st.markdown(f"**Final Score:** {scores['final_score']:.2f}")
                        st.markdown(f"**Keyword Match Score:** {scores['keyword_score']:.2f}")
                        st.markdown(f"**Resume Structure Score:** {scores['structure_score']:.2f}")
                        st.markdown(f"**Skill Match Score:** {scores['skill_match_score']:.2f}")
                        st.markdown(f"**Years of Experience:** {scores['experience_years']}")
                        st.markdown(f"**Contact Info:** {scores['contact_info']}")
                    st.write("---")
        except Exception as e:
            st.error(f"An error occurred while processing the resumes: {str(e)}", icon="🚨")
    else:
        st.error("Please fill in all fields and upload at least one resume.", icon="⚠️")

