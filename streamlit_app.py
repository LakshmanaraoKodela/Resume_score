# import streamlit as st
# import nltk
# from app import analyze_multiple_resumes, download_nltk_resources
# import time
 
# # Set page configuration
# st.set_page_config(page_title="ATS Resume Analyzer", layout="wide", initial_sidebar_state="expanded")
 
# # Custom function for a styled header
# def styled_header(text, color="#4CAF50"):
#     st.markdown(f'<h1 style="text-align: center; color: {color};">{text}</h1>', unsafe_allow_html=True)
 
# # Initialize session state for navigation
# if 'page' not in st.session_state:
#     st.session_state.page = "Home"
 
# # Callback function to update page
# def navigate_to(page):
#     st.session_state.page = page
 
# # Sidebar for app navigation
# st.sidebar.title("Navigation")
# st.sidebar.button("Home", on_click=navigate_to, args=("Home",))
# st.sidebar.button("Analyze Resumes", on_click=navigate_to, args=("Analyze Resumes",))
# st.sidebar.button("About", on_click=navigate_to, args=("About",))
 
# # Main content based on the current page
# if st.session_state.page == "Home":
#     styled_header("Welcome to ATS Score Analyzer!")
#     st.write("Optimize your hiring process with our advanced ATS Resume Analyzer.")
#     # Animated progress bar
#     progress_bar = st.progress(0)
#     for percent_complete in range(100):
#         time.sleep(0.01)
#         progress_bar.progress(percent_complete + 1)
#     st.success("Ready to analyze resumes!")
#     # Call-to-action button
#     st.button("Start Analyzing", on_click=navigate_to, args=("Analyze Resumes",))
 
# elif st.session_state.page == "Analyze Resumes":
#     styled_header("ATS Score Analyzer")
 
#     # Download NLTK resources
#     with st.spinner('Initializing NLTK resources...'):
#         download_nltk_resources()
 
#     # Job Description input with expandable section
#     with st.expander("Job Description", expanded=True):
#         job_description = st.text_area("Enter Job Description", height=200)
#         if job_description:
#             st.info("Job Description Preview:")
#             st.write(job_description)
 
#     # Skills input with chips
#     skills = st.text_input("Enter Required Skills (comma-separated)")
#     if skills:
#         skills = [skill.strip() for skill in skills.split(",")]
#         st.write("Skills Required:")
#         for skill in skills:
#             st.markdown(f'<span style="background-color: #e0e0e0; padding: 5px 10px; border-radius: 20px; margin-right: 5px;">{skill}</span>', unsafe_allow_html=True)
 
#     # Experience input with slider
#     experience_years = st.slider("Required Experience (in years)", 0, 20, 2)
#     st.write(f"Looking for candidates with {experience_years} years of experience")
 
#     # File upload with drag and drop
#     uploaded_files = st.file_uploader("Upload Resumes", type=["pdf", "docx"], accept_multiple_files=True)
#     if uploaded_files:
#         st.success(f"{len(uploaded_files)} resume(s) uploaded successfully!")
 
#     # Analysis button with loading animation
#     if st.button("Analyze Resumes", key="analyze_button"):
#         if job_description and skills and experience_years > 0 and uploaded_files:
#             with st.spinner('Analyzing resumes... Please wait.'):
#                 resume_paths = []
#                 for uploaded_file in uploaded_files:
#                     with open(uploaded_file.name, "wb") as f:
#                         f.write(uploaded_file.getbuffer())
#                         resume_paths.append(uploaded_file.name)
#                 try:
#                     results = analyze_multiple_resumes(resume_paths, job_description, skills, experience_years)
#                     st.subheader("Analysis Results:")
#                     for resume_name, scores in results.items():
#                         with st.expander(f"Results for {resume_name}", expanded=True):
#                             if 'error' in scores:
#                                 st.error(f"Error processing this resume: {scores['error']}")
#                             else:
#                                 col1, col2, col3 = st.columns(3)
#                                 col1.metric("Final Score", f"{scores['final_score']:.2f}")
#                                 col2.metric("Keyword Match", f"{scores['keyword_score']:.2f}")
#                                 col3.metric("Structure Score", f"{scores['structure_score']:.2f}")
#                                 st.write(f"**Skill Match Score:** {scores['skill_match_score']:.2f}")
#                                 st.write(f"**Years of Experience:** {scores['experience_years']}")
#                                 st.write(f"**Contact Info:** {scores['contact_info']}")
#                                 # Visualize scores with a bar chart
#                                 chart_data = {
#                                     'Metric': ['Final Score', 'Keyword Match', 'Structure Score', 'Skill Match'],
#                                     'Score': [scores['final_score'], scores['keyword_score'], scores['structure_score'], scores['skill_match_score']]
#                                 }
#                                 st.bar_chart(chart_data, x='Metric', y='Score', use_container_width=True)
#                 except Exception as e:
#                     st.error(f"An error occurred while processing the resumes: {str(e)}")
#         else:
#             st.warning("Please fill in all fields and upload at least one resume.")
 
# elif st.session_state.page == "About":
#     styled_header("About ATS Score Analyzer")
#     st.write("""
#     Our ATS Score Analyzer is a cutting-edge tool designed to streamline your hiring process. 
#     By leveraging advanced natural language processing techniques, we provide comprehensive 
#     insights into each resume, helping you identify the best candidates quickly and efficiently.
#     Key Features:
#     - Automated resume scoring
#     - Keyword matching
#     - Skills assessment
#     - Experience verification
#     - Resume structure analysis
#     Start optimizing your recruitment process today!
#     """)
#     # Add a fun fact or tip
#     st.info("💡 Did you know? On average, recruiters spend only 7.4 seconds looking at a resume!")
 
# # Footer
# st.markdown("---")
# st.markdown("© 2024 ATS Score Analyzer. All rights reserved.")
#-----------------------------------------------------------------------------------------------------------------------------------
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
#------------------------------------------------------------------------------------------------------------------------

# good result
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


#-----------------------------------------------------------------------------------------------------------
# import streamlit as st
# import nltk
# from app import analyze_multiple_resumes, download_nltk_resources

# # Set page configuration
# st.set_page_config(page_title="ATS Resume Analyzer", layout="wide")

# # Sidebar Navigation
# st.sidebar.title("Navigation")
# options = st.sidebar.radio("Go to", ['Home', 'Analyze Resume', 'About'])

# # NLTK resource initialization
# with st.spinner('Initializing NLP resources...'):
#     download_nltk_resources()

# # Home Page
# if options == 'Home':
#     st.markdown('<h1 style="text-align: center; color: #4CAF50;">ATS Score Analyzer</h1>', unsafe_allow_html=True)
#     st.write("""
#         Welcome to the **ATS Resume Analyzer**! This application helps recruiters assess resumes based on how well they match a given job description, considering factors such as:
#         - Keyword matches
#         - Skills alignment
#         - Years of experience
#         - Resume structure and contact information
        
#         Use the **Analyze Resume** section to upload resumes and view their ATS scores. You can also learn more about how the app works in the **About** section.
#     """)
#     st.image("https://www.example.com/welcome_image.png", caption="Optimize your hiring process with ATS Score Analyzer", use_column_width=True)

# # Analyze Resume Page (Main Functionality)
# elif options == 'Analyze Resume':
#     st.markdown('<h2 style="text-align: center; color: #4CAF50;">Analyze Resumes</h2>', unsafe_allow_html=True)
    
#     # Job Description input
#     job_description = st.text_area("Enter Job Description", height=300, placeholder="Paste the job description here...")
#     if job_description:
#         st.subheader("Job Description Preview:")
#         st.info(job_description)

#     # Skills input
#     skills = st.text_input("Enter Skills (comma-separated)", placeholder="e.g., Python, SQL, Machine Learning")
#     if skills:
#         skills = [skill.strip() for skill in skills.split(",")]
#         st.subheader("Skills Preview:")
#         st.write(", ".join(skills))

#     # Experience input
#     experience_years = st.number_input("Enter Required Experience (in years)", min_value=0)

#     # File upload
#     uploaded_files = st.file_uploader("Upload Resumes (PDF or DOCX)", type=["pdf", "docx"], accept_multiple_files=True)

#     if st.button("Analyze Resumes"):
#         if job_description and skills and experience_years > 0 and uploaded_files:
#             resume_paths = []
#             for uploaded_file in uploaded_files:
#                 with open(uploaded_file.name, "wb") as f:
#                     f.write(uploaded_file.getbuffer())
#                     resume_paths.append(uploaded_file.name)
#             try:
#                 results = analyze_multiple_resumes(resume_paths, job_description, skills, experience_years)
#                 st.subheader("Resume Scores:")
#                 for resume_name, scores in results.items():
#                     st.write(f"### {resume_name}")
#                     if 'error' in scores:
#                         st.error(f"Error processing this resume: {scores['error']}")
#                     else:
#                         st.write(f"**Final Score:** {scores['final_score']:.2f}")
#                         st.write(f"**Keyword Match Score:** {scores['keyword_score']:.2f}")
#                         st.write(f"**Resume Structure Score:** {scores['structure_score']:.2f}")
#                         st.write(f"**Skill Match Score:** {scores['skill_match_score']:.2f}")
#                         st.write(f"**Years of Experience:** {scores['experience_years']}")
#                         st.write(f"**Contact Info:** {scores['contact_info']}")
#                     st.markdown("---")
#             except Exception as e:
#                 st.error(f"An error occurred while processing the resumes: {str(e)}")
#         else:
#             st.error("Please fill in all fields and upload at least one resume.")

# # About Page
# elif options == 'About':
#     st.markdown('<h2 style="text-align: center; color: #4CAF50;">About ATS Resume Analyzer</h2>', unsafe_allow_html=True)
#     st.write("""
#         **ATS Resume Analyzer** is a tool designed to help recruiters streamline the resume evaluation process. 
#         The tool calculates scores based on:
#         - Keyword matches between resumes and job descriptions
#         - The relevance of skills
#         - Years of experience
#         - Resume structure and completeness

#         This tool leverages natural language processing (NLP) techniques to understand the contents of resumes and job descriptions, providing recruiters with a data-driven way to assess candidate fit.
        
#         The **Analyze Resume** section allows you to upload multiple resumes and view a detailed breakdown of their scores. You can use this information to make more informed hiring decisions.
#     """)
#     st.image("https://www.example.com/about_image.png", caption="Streamline your hiring process", use_column_width=True)
#--------------------------------------------------------------------------------
# import streamlit as st
# import nltk
# from app import analyze_multiple_resumes, download_nltk_resources

# # Set page configuration
# st.set_page_config(page_title="ATS Resume Analyzer", layout="wide")

# # Sidebar Navigation
# st.sidebar.title("Navigation")
# options = st.sidebar.radio("Go to", ['Home', 'Analyze Resume', 'About'])

# # NLTK resource initialization
# with st.spinner('Initializing NLP resources...'):
#     download_nltk_resources()

# # Home Page
# if options == 'Home':
#     st.markdown('<h1 style="text-align: center; color: #4CAF50;">ATS Score Analyzer</h1>', unsafe_allow_html=True)
#     st.write("""
#         Welcome to the **ATS Resume Analyzer**! This application helps recruiters assess resumes based on how well they match a given job description, considering factors such as:
#         - Keyword matches
#         - Skills alignment
#         - Years of experience
#         - Resume structure and contact information
        
#         Use the **Analyze Resume** section to upload resumes and view their ATS scores. You can also learn more about how the app works in the **About** section.
#     """)
#     st.image("https://www.example.com/welcome_image.png", caption="Optimize your hiring process with ATS Score Analyzer", use_column_width=True)

# # Analyze Resume Page (Main Functionality)
# elif options == 'Analyze Resume':
#     st.markdown('<h2 style="text-align: center; color: #4CAF50;">Analyze Resumes</h2>', unsafe_allow_html=True)
    
#     # Job Description input
#     job_description = st.text_area("Enter Job Description", height=300, placeholder="Paste the job description here...")
#     if job_description:
#         st.subheader("Job Description Preview:")
#         st.info(job_description)

#     # Skills input
#     skills = st.text_input("Enter Skills (comma-separated)", placeholder="e.g., Python, SQL, Machine Learning")
#     if skills:
#         skills = [skill.strip() for skill in skills.split(",")]
#         st.subheader("Skills Preview:")
#         st.write(", ".join(skills))

#     # Experience input
#     experience_years = st.number_input("Enter Required Experience (in years)", min_value=0)

#     # File upload
#     uploaded_files = st.file_uploader("Upload Resumes (PDF or DOCX)", type=["pdf", "docx"], accept_multiple_files=True)

#     if st.button("Analyze Resumes"):
#         if job_description and skills and experience_years > 0 and uploaded_files:
#             resume_paths = []
#             for uploaded_file in uploaded_files:
#                 with open(uploaded_file.name, "wb") as f:
#                     f.write(uploaded_file.getbuffer())
#                     resume_paths.append(uploaded_file.name)
#             try:
#                 results = analyze_multiple_resumes(resume_paths, job_description, skills, experience_years)
#                 st.subheader("Resume Scores:")
#                 for resume_name, scores in results.items():
#                     st.write(f"### {resume_name}")
#                     if 'error' in scores:
#                         st.error(f"Error processing this resume: {scores['error']}")
#                     else:
#                         st.write(f"**Final Score:** {scores['final_score']:.2f}")
#                         st.write(f"**Keyword Match Score:** {scores['keyword_score']:.2f}")
#                         st.write(f"**Resume Structure Score:** {scores['structure_score']:.2f}")
#                         st.write(f"**Skill Match Score:** {scores['skill_match_score']:.2f}")
#                         st.write(f"**Years of Experience:** {scores['experience_years']}")
#                         st.write(f"**Contact Info:** {scores['contact_info']}")
#                     st.markdown("---")
#             except Exception as e:
#                 st.error(f"An error occurred while processing the resumes: {str(e)}")
#         else:
#             st.error("Please fill in all fields and upload at least one resume.")

# # About Page
# elif options == 'About':
#     st.markdown('<h2 style="text-align: center; color: #4CAF50;">About ATS Resume Analyzer</h2>', unsafe_allow_html=True)
#     st.write("""
#         **ATS Resume Analyzer** is a tool designed to help recruiters streamline the resume evaluation process. 
#         The tool calculates scores based on:
#         - Keyword matches between resumes and job descriptions
#         - The relevance of skills
#         - Years of experience
#         - Resume structure and completeness

#         This tool leverages natural language processing (NLP) techniques to understand the contents of resumes and job descriptions, providing recruiters with a data-driven way to assess candidate fit.
        
#         The **Analyze Resume** section allows you to upload multiple resumes and view a detailed breakdown of their scores. You can use this information to make more informed hiring decisions.
#     """)
#     st.image("https://www.example.com/about_image.png", caption="Streamline your hiring process", use_column_width=True)

# error no
#------------------------

# import streamlit as st
# import nltk
# import csv
# import io  # Import io to create a file-like object
# from app import analyze_multiple_resumes, download_nltk_resources

# # Set page configuration
# st.set_page_config(page_title="ATS Resume Analyzer", layout="wide")

# # Sidebar Navigation
# st.sidebar.title("Navigation")
# options = st.sidebar.radio("Go to", ['Home', 'Analyze Resume', 'About'])

# # NLTK resource initialization
# with st.spinner('Initializing NLP resources...'):
#     download_nltk_resources()

# # Home Page
# if options == 'Home':
#     st.markdown('<h1 style="text-align: center; color: #4CAF50;">ATS Score Analyzer</h1>', unsafe_allow_html=True)
#     st.write("""
#         Welcome to the **ATS Resume Analyzer**! This application helps recruiters assess resumes based on how well they match a given job description, considering factors such as:
#         - Keyword matches
#         - Skills alignment
#         - Years of experience
#         - Resume structure and contact information
        
#         Use the **Analyze Resume** section to upload resumes and view their ATS scores. You can also learn more about how the app works in the **About** section.
#     """)
#     st.image("https://www.example.com/welcome_image.png", caption="Optimize your hiring process with ATS Score Analyzer", use_column_width=True)


# # Analyze Resume Page (Main Functionality)
# elif options == 'Analyze Resume':
#     st.markdown('<h2 style="text-align: center; color: #4CAF50;">Analyze Resumes</h2>', unsafe_allow_html=True)
    
#     # Job Description input
#     job_description = st.text_area("Enter Job Description", height=300, placeholder="Paste the job description here...")
#     if job_description:
#         st.subheader("Job Description Preview:")
#         st.info(job_description)

#     # Skills input
#     skills = st.text_input("Enter Skills (comma-separated)", placeholder="e.g., Python, SQL, Machine Learning")
#     if skills:
#         skills = [skill.strip() for skill in skills.split(",")]
#         st.subheader("Skills Preview:")
#         st.write(", ".join(skills))

#     # Experience input
#     experience_years = st.number_input("Enter Required Experience (in years)", min_value=0)

#     # File upload
#     uploaded_files = st.file_uploader("Upload Resumes (PDF or DOCX)", type=["pdf", "docx"], accept_multiple_files=True)

#     if st.button("Analyze Resumes"):
#         if job_description and skills and experience_years > 0 and uploaded_files:
#             resume_paths = []
#             for uploaded_file in uploaded_files:
#                 with open(uploaded_file.name, "wb") as f:
#                     f.write(uploaded_file.getbuffer())
#                     resume_paths.append(uploaded_file.name)
#             try:
#                 results = analyze_multiple_resumes(resume_paths, job_description, skills, experience_years)
#                 st.subheader("Resume Scores:")
                
#                 # Prepare CSV data
#                 csv_data = "Resume Name,Final Score,Keyword Match Score,Resume Structure Score,Skill Match Score,Years of Experience,Contact Info\n"
                
#                 for resume_name, scores in results.items():
#                     st.write(f"### {resume_name}")
#                     if 'error' in scores:
#                         st.error(f"Error processing this resume: {scores['error']}")
#                     else:
#                         st.write(f"**Final Score:** {scores['final_score']:.2f}")
#                         st.write(f"**Keyword Match Score:** {scores['keyword_score']:.2f}")
#                         st.write(f"**Resume Structure Score:** {scores['structure_score']:.2f}")
#                         st.write(f"**Skill Match Score:** {scores['skill_match_score']:.2f}")
#                         st.write(f"**Years of Experience:** {scores['experience_years']}")
#                         st.write(f"**Contact Info:** {scores['contact_info']}")

#                         # Append scores to the CSV data string
#                         csv_data += f"{resume_name},{scores['final_score']:.2f},{scores['keyword_score']:.2f},{scores['structure_score']:.2f},{scores['skill_match_score']:.2f},{scores['experience_years']},{scores['contact_info']}\n"
                    
#                     st.markdown("---")

#                 # Create a download button for CSV
#                 if csv_data:
#                     # Create a StringIO object to simulate a file
#                     output = io.StringIO()
#                     output.write(csv_data)
#                     output.seek(0)  # Move cursor to the start of the stream

#                     st.download_button(
#                         label="Download Scores as CSV",
#                         data=output.getvalue(),
#                         file_name='resume_scores.csv',
#                         mime='text/csv',
#                     )

#             except Exception as e:
#                 st.error(f"An error occurred while processing the resumes: {str(e)}")
#         else:
#             st.error("Please fill in all fields and upload at least one resume.")

# # About Page
# elif options == 'About':
#     st.markdown('<h2 style="text-align: center; color: #4CAF50;">About ATS Resume Analyzer</h2>', unsafe_allow_html=True)
#     st.write("""
#         **ATS Resume Analyzer** is a tool designed to help recruiters streamline the resume evaluation process. 
#         The tool calculates scores based on:
#         - Keyword matches between resumes and job descriptions
#         - The relevance of skills
#         - Years of experience
#         - Resume structure and completeness

#         This tool leverages natural language processing (NLP) techniques to understand the contents of resumes and job descriptions, providing recruiters with a data-driven way to assess candidate fit.
        
#         The **Analyze Resume** section allows you to upload multiple resumes and view a detailed breakdown of their scores. You can use this information to make more informed hiring decisions.
#     """)
#     st.image("https://www.example.com/about_image.png", caption="Streamline your hiring process", use_column_width=True)
#---------------------------

import streamlit as st
import nltk
import io
import csv
from app import analyze_multiple_resumes, download_nltk_resources

# Set page configuration
st.set_page_config(page_title="ATS Resume Analyzer", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Analyze Resume", "About"])

# Download NLTK resources
with st.spinner("Initializing NLP resources..."):
    download_nltk_resources()

# Custom header function for styled text
def styled_header(text, color="#4CAF50"):
    st.markdown(f'<h1 style="text-align: center; color: {color};">{text}</h1>', unsafe_allow_html=True)

# Home Page
if page == "Home":
    styled_header("ATS Score Analyzer")
    st.write("""
        Welcome to the **ATS Resume Analyzer**! This business tool helps recruiters analyze resumes by matching them against job descriptions. It scores resumes based on:
        - Keyword matches
        - Skill relevance
        - Years of experience
        - Resume structure and completeness

        Use the **Analyze Resume** section to start uploading resumes and viewing ATS scores. Explore how the app works in the **About** section.
    """)
    st.image("https://www.example.com/welcome_image.png", caption="Optimize your hiring process with ATS Score Analyzer", use_column_width=True)
    st.success("Ready to analyze resumes!")


# Analyze Resume Page
elif page == "Analyze Resume":
    styled_header("Analyze Resumes")
    
    # Job Description input
    job_description = st.text_area("Enter Job Description", height=300, placeholder="Paste the job description here...")
    if job_description:
        st.subheader("Job Description Preview:")
        st.info(job_description)

    # Skills input with validation
    skills = st.text_input("Enter Skills (comma-separated)", placeholder="e.g., Python, SQL, Machine Learning")
    if skills:
        skills = [skill.strip() for skill in skills.split(",")]
        st.subheader("Skills Preview:")
        st.write(", ".join(skills))

    # Experience input
    experience_years = st.number_input("Enter Required Experience (in years)", min_value=0, value=1)

    # File upload with multi-file support
    uploaded_files = st.file_uploader("Upload Resumes (PDF or DOCX)", type=["pdf", "docx"], accept_multiple_files=True)

    if st.button("Analyze Resumes"):
        if job_description and skills and experience_years > 0 and uploaded_files:
            resume_paths = []
            for uploaded_file in uploaded_files:
                with open(uploaded_file.name, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                    resume_paths.append(uploaded_file.name)

            try:
                results = analyze_multiple_resumes(resume_paths, job_description, skills, experience_years)
                st.subheader("Resume Scores:")
                
                csv_data = "Resume Name,Final Score,Keyword Match Score,Resume Structure Score,Skill Match Score,Years of Experience,Contact Info\n"
                
                for resume_name, scores in results.items():
                    st.write(f"### {resume_name}")
                    if 'error' in scores:
                        st.error(f"Error processing resume: {scores['error']}")
                    else:
                        # Detailed score breakdown
                        st.write(f"**Final Score:** {scores['final_score']:.2f}")
                        st.write(f"**Keyword Match Score:** {scores['keyword_score']:.2f}")
                        st.write(f"**Skill Match Score:** {scores['skill_match_score']:.2f}")
                        st.write(f"**Years of Experience:** {scores['experience_years']}")
                        st.write(f"**Contact Info:** {scores['contact_info']}")

                        csv_data += f"{resume_name},{scores['final_score']:.2f},{scores['keyword_score']:.2f},{scores['structure_score']:.2f},{scores['skill_match_score']:.2f},{scores['experience_years']},{scores['contact_info']}\n"

                    st.markdown("---")

                # CSV Download
                if csv_data:
                    output = io.StringIO()
                    output.write(csv_data)
                    output.seek(0)

                    st.download_button(
                        label="Download Scores as CSV",
                        data=output.getvalue(),
                        file_name="resume_scores.csv",
                        mime="text/csv"
                    )

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
        else:
            st.error("Please fill in all fields and upload resumes.")

# About Page
elif page == "About":
    styled_header("About ATS Resume Analyzer")
    st.write("""
        **ATS Resume Analyzer** is built for recruiters to streamline the resume screening process. 
        It uses natural language processing to score resumes based on keyword matches, skills, and experience, providing a structured way to evaluate candidate fit.
        
        Key features:
        - Automated resume scoring based on job descriptions
        - Skill and experience assessment
        - Resume structure analysis
    """)
    # Add a fun fact or tip
    st.info("💡 Did you know? On average, recruiters spend only 7.4 seconds looking at a resume!")
    st.image("https://www.example.com/about_image.png", caption="Streamline your hiring process", use_column_width=True)
