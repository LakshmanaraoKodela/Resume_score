# import streamlit as st
# import nltk
# from app import analyze_multiple_resumes, download_nltk_resources

# # Download NLTK resources at the start of the app
# with st.spinner('Initializing NLTK resources...'):
#     download_nltk_resources()
# st.success('NLTK resources initialized successfully!')

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
import pandas as pd
import plotly.graph_objects as go
from app import analyze_multiple_resumes, download_nltk_resources

# Set page config
st.set_page_config(page_title="ATS Resume Scorer", page_icon="📄", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .main {
        background-color: #f0f2f6;
        padding: 20px;
    }
    .stButton>button {
        width: 100%;
    }
    .stProgress>div>div>div>div {
        background-color: #4CAF50;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'results' not in st.session_state:
    st.session_state.results = None

# Sidebar
with st.sidebar:
    st.image("https://your-logo-url.com", width=200)  # Replace with your logo URL
    st.title("ATS Resume Scorer")
    st.markdown("Upload resumes and compare them against job descriptions.")

    # Download NLTK resources
    with st.spinner('Initializing NLTK resources...'):
        download_nltk_resources()
    st.success('NLTK resources initialized successfully!')

# Main content
st.title("Resume ATS Scoring Application")

# Create two columns
col1, col2 = st.columns(2)

with col1:
    # Job Description input
    job_description = st.text_area("Enter Job Description", height=200)

    # Skills input
    skills = st.text_input("Enter Required Skills (comma-separated)")

    # Experience input
    experience_years = st.number_input("Enter Required Experience (in years)", min_value=0)

with col2:
    # File upload
    uploaded_files = st.file_uploader("Upload Resumes", type=["pdf", "docx"], accept_multiple_files=True)

    if uploaded_files:
        st.write(f"Uploaded {len(uploaded_files)} resume(s)")
        for file in uploaded_files:
            st.write(f"- {file.name}")

# Process button
if st.button("Analyze Resumes"):
    if job_description and skills and experience_years > 0 and uploaded_files:
        with st.spinner("Analyzing resumes..."):
            resume_paths = []
            for uploaded_file in uploaded_files:
                with open(uploaded_file.name, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                    resume_paths.append(uploaded_file.name)
            
            skills_list = [skill.strip() for skill in skills.split(",")]
            st.session_state.results = analyze_multiple_resumes(resume_paths, job_description, skills_list, experience_years)
        
        st.success("Analysis complete!")
    else:
        st.error("Please fill in all fields and upload at least one resume.")

# Display results
if st.session_state.results:
    st.subheader("Resume Scores")

    for resume_name, scores in st.session_state.results.items():
        with st.expander(f"{resume_name} - Score: {scores['final_score']:.2f}"):
            col1, col2 = st.columns(2)
            
            with col1:
                # Total score progress bar
                st.subheader("Total Score")
                st.progress(scores['final_score'] / 100)
                st.write(f"{scores['final_score']:.2f}%")

                # Radar chart
                categories = ['Keyword Match', 'Resume Structure', 'Skill Match', 'Experience']
                values = [scores['keyword_score'], scores['structure_score'], 
                          scores['skill_match_score'], min(scores['experience_years'], experience_years) * 10]

                fig = go.Figure(data=go.Scatterpolar(
                    r=values,
                    theta=categories,
                    fill='toself'
                ))

                fig.update_layout(
                    polar=dict(
                        radialaxis=dict(visible=True, range=[0, 100])
                    ),
                    showlegend=False
                )

                st.plotly_chart(fig, use_container_width=True)

            with col2:
                st.subheader("Detailed Scores")
                st.write(f"**Keyword Match Score:** {scores['keyword_score']:.2f}")
                st.write(f"**Resume Structure Score:** {scores['structure_score']:.2f}")
                st.write(f"**Skill Match Score:** {scores['skill_match_score']:.2f}")
                st.write(f"**Years of Experience:** {scores['experience_years']}")

                st.subheader("Skills")
                skill_df = pd.DataFrame({
                    'Resume Skills': list(scores['resume_skills']),
                    'Job Skills': list(scores['job_skills'])
                })
                st.dataframe(skill_df)

                st.subheader("Contact Information")
                for key, value in scores['contact_info'].items():
                    st.write(f"**{key.capitalize()}:** {', '.join(value)}")

    # Compare resumes
    st.subheader("Resume Comparison")
    comparison_df = pd.DataFrame({
        resume: {
            'Total Score': scores['final_score'],
            'Keyword Match': scores['keyword_score'],
            'Resume Structure': scores['structure_score'],
            'Skill Match': scores['skill_match_score'],
            'Experience Years': scores['experience_years']
        } for resume, scores in st.session_state.results.items()
    }).T

    st.dataframe(comparison_df.style.highlight_max(axis=0))

    # Download results
    csv = comparison_df.to_csv(index=True)
    st.download_button(
        label="Download Results as CSV",
        data=csv,
        file_name="resume_comparison.csv",
        mime="text/csv",
    )

