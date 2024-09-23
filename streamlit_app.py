import streamlit as st
import pandas as pd
import base64
from io import BytesIO
from app import analyze_multiple_resumes, download_nltk_resources

# Set page configuration
st.set_page_config(page_title="ATS Resume Analyzer", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    .main {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }
    .stTextInput, .stTextArea, .stNumberInput {
        background-color: #ffffff;
        border-radius: 5px;
        padding: 10px;
        border: 1px solid #e0e0e0;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        border: none;
        padding: 10px 20px;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .results-container {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
    }
    .result-item {
        border-bottom: 1px solid #e0e0e0;
        padding: 10px 0;
    }
    .result-item:last-child {
        border-bottom: none;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 style="text-align: center; color: #4CAF50;">ATS Resume Analyzer</h1>', unsafe_allow_html=True)

# Download NLTK resources at the start of the app
with st.spinner('Initializing NLTK resources...'):
    download_nltk_resources()

# Create columns for input fields
col1, col2 = st.columns(2)

with col1:
    # Job Description input
    job_description = st.text_area("Enter Job Description", height=200)

with col2:
    # Skills input
    skills = st.text_input("Enter Skills (comma-separated)")
    # Experience input
    experience_years = st.number_input("Enter Required Experience (in years)", min_value=0)
    # File upload
    uploaded_files = st.file_uploader("Upload Resumes", type=["pdf", "docx"], accept_multiple_files=True)

if st.button("Analyze Resumes"):
    if job_description and skills and experience_years > 0 and uploaded_files:
        skills = [skill.strip() for skill in skills.split(",")]
        resume_paths = []
        for uploaded_file in uploaded_files:
            with open(uploaded_file.name, "wb") as f:
                f.write(uploaded_file.getbuffer())
                resume_paths.append(uploaded_file.name)
        
        try:
            results = analyze_multiple_resumes(resume_paths, job_description, skills, experience_years)
        
            st.markdown('<div class="results-container">', unsafe_allow_html=True)
            st.subheader("Resume Scores:")
            for resume_name, scores in results.items():
                st.markdown(f'<div class="result-item">', unsafe_allow_html=True)
                st.write(f"### {resume_name}")
                if 'error' in scores:
                    st.error(f"Error processing this resume: {scores['error']}")
                else:
                    st.write(f"**Final Score:** {scores['final_score']:.2f}")
                    st.write(f"**Keyword Match Score:** {scores['keyword_score']:.2f}")
                    st.write(f"**Resume Structure Score:** {scores['structure_score']:.2f}")
                    st.write(f"**Skill Match Score:** {scores['skill_match_score']:.2f}")
                    st.write(f"**Years of Experience:** {scores['experience_years']}")
                    st.write(f"**Contact Info:** {scores['contact_info']}")
                st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            # Convert results to DataFrame
            df = pd.DataFrame.from_dict(results, orient='index')
            df = df.reset_index().rename(columns={'index': 'Resume Name'})

            # Download button for CSV
            csv = df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="resume_scores.csv" class="download-button">Download Results as CSV</a>'
            st.markdown(href, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"An error occurred while processing the resumes: {str(e)}")
    else:
        st.error("Please fill in all fields and upload at least one resume.")
