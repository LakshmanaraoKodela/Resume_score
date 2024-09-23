import streamlit as st
import nltk
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

# Define a function to determine pipe color based on the score
def get_color_for_score(score):
    if score >= 80:
        return '#4CAF50'  # Green
    elif 60 <= score < 80:
        return '#FFC107'  # Yellow
    elif 40 <= score < 60:
        return '#FF9800'  # Orange
    else:
        return '#F44336'  # Red

# Add borders and pipe color for each resume based on score
if st.button("View Scores"):
    if job_description and skills and experience_years > 0 and uploaded_files:
        resume_paths = []
        for uploaded_file in uploaded_files:
            with open(uploaded_file.name, "wb") as f:
                f.write(uploaded_file.getbuffer())
                resume_paths.append(uploaded_file.name)
        try:
            results = analyze_multiple_resumes(resume_paths, job_description, skills, experience_years)
            st.subheader("Resume Scores:")
            for resume_name, scores in results.items():
                if 'error' in scores:
                    st.error(f"Error processing this resume: {scores['error']}")
                else:
                    color = get_color_for_score(scores['final_score'])
                    
                    # Adding border and colored pipe
                    st.markdown(f"""
                        <div style="
                            border: 4px solid black;
                            padding: 10px;
                            margin-bottom: 10px;
                            position: relative;">
                            <div style="
                                background-color: {color};
                                width: 10px;
                                height: 100%;
                                position: absolute;
                                left: 0;
                                top: 0;">
                            </div>
                            <div style="margin-left: 20px;">
                                <h3>{resume_name}</h3>
                                <p><b>Final Score:</b> {scores['final_score']:.2f}</p>
                                <p><b>Keyword Match Score:</b> {scores['keyword_score']:.2f}</p>
                                <p><b>Resume Structure Score:</b> {scores['structure_score']:.2f}</p>
                                <p><b>Skill Match Score:</b> {scores['skill_match_score']:.2f}</p>
                                <p><b>Years of Experience:</b> {scores['experience_years']}</p>
                                <p><b>Contact Info:</b> {scores['contact_info']}</p>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                    st.write("---")
        except Exception as e:
            st.error(f"An error occurred while processing the resumes: {str(e)}")
    else:
        st.error("Please fill in all fields and upload at least one resume.")
