import streamlit as st
from app import analyze_multiple_resumes

st.title("Resume ATS Scoring Application")

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

        results = analyze_multiple_resumes(resume_paths, job_description, skills, experience_years)
        
        st.subheader("Resume Scores:")
        for resume_name, scores in results.items():
            st.write(f"### {resume_name}")
            st.write(f"**Final Score:** {scores['final_score']:.2f}")
            st.write(f"**Keyword Match Score:** {scores['keyword_score']:.2f}")
            st.write(f"**Resume Structure Score:** {scores['structure_score']:.2f}")
            st.write(f"**Skill Match Score:** {scores['skill_match_score']:.2f}")
            st.write(f"**Years of Experience:** {scores['experience_years']}")
            st.write(f"**Contact Info:** {scores['contact_info']}")
            st.write("---")
    else:
        st.error("Please fill in all fields and upload at least one resume.")
