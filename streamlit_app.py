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
    st.success("Ready to analyze resumes!")
    st.image("data:image/jpeg;base64,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", caption="Optimize your hiring process with ATS Score Analyzer", use_column_width=True)

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

