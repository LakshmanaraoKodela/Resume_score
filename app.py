import os
import re
import PyPDF2
import docx
import textract
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from word2number import w2n

# Function to download NLTK resources
def download_nltk_resources():
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt', quiet=True)
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords', quiet=True)

download_nltk_resources()

def extract_text(file_path):
    _, file_extension = os.path.splitext(file_path)
    if file_extension.lower() == '.pdf':
        return extract_text_from_pdf(file_path)
    elif file_extension.lower() in ['.docx', '.doc']:
        return extract_text_from_docx(file_path)
    else:
        return extract_text_from_other(file_path)

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        return " ".join(page.extract_text() for page in reader.pages)

def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    return " ".join(paragraph.text for paragraph in doc.paragraphs)

def extract_text_from_other(file_path):
    return textract.process(file_path).decode('utf-8')

def preprocess_text(text):
    tokens = nltk.word_tokenize(text)
    return " ".join(token.lower() for token in tokens if token.isalpha())

def extract_skills(text, skills):
    skills_found = set()
    for skill in skills:
        if skill.lower() in text.lower():
            skills_found.add(skill.lower())
    return skills_found

def extract_contact_info(text):
    phone_pattern = r'(\+?\d{1,3}[- ]?)?\d{10}'
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    linkedin_pattern = r'(https?://)?(www\.)?linkedin\.com/in/[A-Za-z0-9-_]+'

    phone_numbers = re.findall(phone_pattern, text)
    emails = re.findall(email_pattern, text)
    linkedin_profiles = re.findall(linkedin_pattern, text)

    return {
        'phone_numbers': phone_numbers,
        'emails': emails,
        'linkedin_profiles': linkedin_profiles
    }

def calculate_keyword_score(resume_text, job_description):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([resume_text, job_description])
    return cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0] * 100

def analyze_resume_structure(resume_text):
    sections = ["summary", "experience", "education", "skills", "projects", "role", "certifications", "work history"]
    score = sum(1 for section in sections if re.search(r'\b' + section + r'\b', resume_text, re.IGNORECASE))
    return (score / len(sections)) * 100

def calculate_skill_match(resume_skills, job_skills):
    matched_skills = resume_skills.intersection(job_skills)
    return (len(matched_skills) / len(job_skills)) * 100 if job_skills else 0

def analyze_experience(resume_text):
    tokens = nltk.word_tokenize(resume_text.lower())
    experience_years = 0
    experience_keywords = ["experience", "work", "working"]

    for i, token in enumerate(tokens):
        if token in experience_keywords and i > 0:
            try:
                prev_token = tokens[i - 1]
                if prev_token.isdigit():
                    experience_years += int(prev_token)
                else:
                    experience_years += w2n.word_to_num(prev_token)
            except (ValueError, IndexError):
                continue

    return experience_years

def calculate_ats_score(resume_path, job_description, skills, experience_years):
    resume_text = extract_text(resume_path)
    preprocessed_resume = preprocess_text(resume_text)
    preprocessed_job = preprocess_text(job_description)
    
    resume_skills = extract_skills(preprocessed_resume, skills)
    job_skills = extract_skills(preprocessed_job, skills)
    
    keyword_score = calculate_keyword_score(preprocessed_resume, preprocessed_job)
    structure_score = analyze_resume_structure(resume_text)
    skill_match_score = calculate_skill_match(resume_skills, job_skills)
    total_experience_years = analyze_experience(resume_text)

    # Adjust weights based on importance
    final_score = (
        keyword_score * 0.4 +
        structure_score * 0.2 +
        skill_match_score * 0.3 +
        min(total_experience_years, experience_years) * 0.1
    )
    
    return {
        'final_score': final_score,
        'keyword_score': keyword_score,
        'structure_score': structure_score,
        'skill_match_score': skill_match_score,
        'experience_years': total_experience_years,
        'resume_skills': resume_skills,
        'job_skills': job_skills,
        'contact_info': extract_contact_info(resume_text)
    }

def analyze_multiple_resumes(resume_paths, job_description, skills, experience_years):
    results = {}
    for resume_path in resume_paths:
        resume_name = os.path.basename(resume_path)
        scores = calculate_ats_score(resume_path, job_description, skills, experience_years)
        results[resume_name] = scores
    return results
