import streamlit as st
from app import extract_text_from_pdf, extract_text_from_docx, calculate_ats_score, load_skills_db

st.title('ATS Resume Scoring Application')

uploaded_file = st.file_uploader("Upload your resume", type=['pdf', 'docx'])
job_description = st.text_area("Enter the Job Description")

if uploaded_file and job_description:
    # Extract text from resume
    if uploaded_file.name.endswith('.pdf'):
        resume_text = extract_text_from_pdf(uploaded_file)
    elif uploaded_file.name.endswith('.docx'):
        resume_text = extract_text_from_docx(uploaded_file)
    
    # Load skills database
    skills_db = load_skills_db('skills_db.json')['skills']
    
    # Calculate ATS score
    scores = calculate_ats_score(resume_text, job_description, skills_db)
    
    # Display the results
    st.subheader(f"ATS Score: {scores['final_score']:.2f}%")
    st.write(f"Keyword Match Score: {scores['keyword_score']:.2f}%")
    st.write(f"Skill Match Score: {scores['skill_match_score']:.2f}%")
    st.write(f"Years of Experience: {scores['experience_years']}")

    # Display additional feedback
    if scores['final_score'] >= 70:
        st.success("Your resume looks great for this job!")
    else:
        st.warning("Consider improving your resume based on the job description.")
