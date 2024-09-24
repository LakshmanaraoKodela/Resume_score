# import os
# import re
# import PyPDF2
# import docx
# import textract
# import nltk
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# from word2number import w2n
# from nltk.tokenize import word_tokenize
 
# def download_nltk_resources():
#     resources = ['punkt', 'averaged_perceptron_tagger', 'maxent_ne_chunker', 'words', 'stopwords', 'punkt_tab']
#     for resource in resources:
#         try:
#             nltk.data.find(f'tokenizers/{resource}')
#         except LookupError:
#             try:
#                 nltk.download(resource, quiet=True)
#             except Exception as e:
#                 print(f"Error downloading {resource}: {str(e)}")
 
# def fallback_tokenize(text):
#     return text.split()
 
# def extract_text(file_path):
#     _, file_extension = os.path.splitext(file_path)
#     if file_extension.lower() == '.pdf':
#         return extract_text_from_pdf(file_path)
#     elif file_extension.lower() in ['.docx', '.doc']:
#         return extract_text_from_docx(file_path)
#     else:
#         return extract_text_from_other(file_path)
 
# def extract_text_from_pdf(pdf_path):
#     with open(pdf_path, 'rb') as file:
#         reader = PyPDF2.PdfReader(file)
#         return " ".join(page.extract_text() for page in reader.pages)
 
# def extract_text_from_docx(docx_path):
#     doc = docx.Document(docx_path)
#     return " ".join(paragraph.text for paragraph in doc.paragraphs)
 
# def extract_text_from_other(file_path):
#     return textract.process(file_path).decode('utf-8')
 
# def preprocess_text(text):
#     try:
#         tokens = word_tokenize(text)
#     except LookupError:
#         print("Warning: NLTK tokenizer not available. Using fallback tokenization.")
#         tokens = fallback_tokenize(text)
#     return " ".join(token.lower() for token in tokens if token.isalpha())
 
# def extract_skills(text, skills):
#     skills_found = set()
#     for skill in skills:
#         if skill.lower() in text.lower():
#             skills_found.add(skill.lower())
#     return skills_found
 
# def extract_contact_info(text):
#     phone_pattern = r'(\+?\d{1,3}[- ]?)?\d{10}'
#     email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
#     linkedin_pattern = r'(https?://)?(www\.)?linkedin\.com/in/[A-Za-z0-9-_]+'
 
#     phone_numbers = re.findall(phone_pattern, text)
#     emails = re.findall(email_pattern, text)
#     linkedin_profiles = re.findall(linkedin_pattern, text)
 
#     return {
#         'phone_numbers': phone_numbers,
#         'emails': emails,
#         'linkedin_profiles': linkedin_profiles
#     }
 
# def calculate_keyword_score(resume_text, job_description):
#     vectorizer = TfidfVectorizer()
#     tfidf_matrix = vectorizer.fit_transform([resume_text, job_description])
#     return cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0] * 100
 
# def analyze_resume_structure(resume_text):
#     sections = ["summary", "experience", "education", "skills", "projects", "role", "certifications", "work history"]
#     try:
#         score = sum(1 for section in sections if section in resume_text.lower().split())
#     except Exception as e:
#         print(f"Error in analyze_resume_structure: {str(e)}")
#         score = 0
#     return (score / len(sections)) * 100
 
# def calculate_skill_match(resume_skills, job_skills):
#     matched_skills = resume_skills.intersection(job_skills)
#     return (len(matched_skills) / len(job_skills)) * 100 if job_skills else 0
 
# def analyze_experience(resume_text):
#     try:
#         tokens = word_tokenize(resume_text.lower())
#     except LookupError:
#         print("Warning: NLTK tokenizer not available. Using fallback tokenization.")
#         tokens = fallback_tokenize(resume_text.lower())
#     experience_years = 0
#     experience_keywords = ["experience", "work", "working"]
 
#     for i, token in enumerate(tokens):
#         if token in experience_keywords and i > 0:
#             try:
#                 prev_token = tokens[i - 1]
#                 if prev_token.isdigit():
#                     experience_years += int(prev_token)
#                 else:
#                     experience_years += w2n.word_to_num(prev_token)
#             except (ValueError, IndexError):
#                 continue
 
#     return experience_years
 
# def calculate_ats_score(resume_path, job_description, skills, experience_years):
#     try:
#         resume_text = extract_text(resume_path)
#         preprocessed_resume = preprocess_text(resume_text)
#         preprocessed_job = preprocess_text(job_description)
#         resume_skills = extract_skills(preprocessed_resume, skills)
#         job_skills = extract_skills(preprocessed_job, skills)
#         keyword_score = calculate_keyword_score(preprocessed_resume, preprocessed_job)
#         structure_score = analyze_resume_structure(resume_text)
#         skill_match_score = calculate_skill_match(resume_skills, job_skills)
#         total_experience_years = analyze_experience(resume_text)
 
#         final_score = (
#             keyword_score * 0.4 +
#             structure_score * 0.2 +
#             skill_match_score * 0.3 +
#             min(total_experience_years, experience_years) * 0.1
#         )
#         return {
#             'final_score': final_score,
#             'keyword_score': keyword_score,
#             'structure_score': structure_score,
#             'skill_match_score': skill_match_score,
#             'experience_years': total_experience_years,
#             'resume_skills': resume_skills,
#             'job_skills': job_skills,
#             'contact_info': extract_contact_info(resume_text)
#         }
#     except Exception as e:
#         return {
#             'error': str(e),
#             'final_score': 0,
#             'keyword_score': 0,
#             'structure_score': 0,
#             'skill_match_score': 0,
#             'experience_years': 0,
#             'resume_skills': set(),
#             'job_skills': set(),
#             'contact_info': {}
#         }
 
# def analyze_multiple_resumes(resume_paths, job_description, skills, experience_years):
#     download_nltk_resources()
#     results = {}
#     for resume_path in resume_paths:
#         try:
#             resume_name = os.path.basename(resume_path)
#             scores = calculate_ats_score(resume_path, job_description, skills, experience_years)
#             results[resume_name] = scores
#         except Exception as e:
#             results[resume_name] = {'error': str(e)}
#     return results
 
# def save_results_to_csv(results):
#     df = pd.DataFrame.from_dict(results, orient='index')
#     csv_file_path = "resume_scores.csv"
#     df.to_csv(csv_file_path)
#     return csv_file_path


import os
import re
import PyPDF2
import docx
import textract
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from word2number import w2n
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import spacy
from fuzzywuzzy import fuzz
import pandas as pd

def download_nltk_resources():
    resources = ['punkt', 'averaged_perceptron_tagger', 'maxent_ne_chunker', 'words', 'stopwords', 'wordnet']
    for resource in resources:
        try:
            nltk.data.find(f'tokenizers/{resource}')
        except LookupError:
            nltk.download(resource, quiet=True)

def load_spacy_model():
    try:
        return spacy.load("en_core_web_sm")
    except OSError:
        print("Downloading spaCy model...")
        spacy.cli.download("en_core_web_sm")
        return spacy.load("en_core_web_sm")

nlp = load_spacy_model()
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

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
    # Tokenize and lemmatize
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if token.is_alpha and token.lemma_ not in stop_words]
    return " ".join(tokens)

def extract_skills(text, skills):
    skills_found = set()
    doc = nlp(text.lower())
    for skill in skills:
        skill_tokens = nlp(skill.lower())
        for token in doc:
            if token.lemma_ in [t.lemma_ for t in skill_tokens]:
                skills_found.add(skill.lower())
                break
    return skills_found

def extract_contact_info(text):
    doc = nlp(text)
    contact_info = {
        'name': '',
        'phone_numbers': [],
        'emails': [],
        'linkedin_profiles': []
    }

    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            contact_info['name'] = ent.text
            break

    phone_pattern = r'(\+?\d{1,3}[- ]?)?\d{10}'
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    linkedin_pattern = r'(https?://)?(www\.)?linkedin\.com/in/[A-Za-z0-9-_]+'

    contact_info['phone_numbers'] = re.findall(phone_pattern, text)
    contact_info['emails'] = re.findall(email_pattern, text)
    contact_info['linkedin_profiles'] = re.findall(linkedin_pattern, text)

    return contact_info

def calculate_keyword_score(resume_text, job_description):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([resume_text, job_description])
    return cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0] * 100

def analyze_resume_structure(resume_text):
    sections = ["summary", "experience", "education", "skills", "projects", "achievements", "certifications"]
    score = sum(1 for section in sections if section in resume_text.lower().split())
    return (score / len(sections)) * 100

def calculate_skill_match(resume_skills, job_skills):
    if not job_skills:
        return 0
    
    matched_skills = set()
    for job_skill in job_skills:
        for resume_skill in resume_skills:
            if fuzz.ratio(job_skill.lower(), resume_skill.lower()) > 80:
                matched_skills.add(job_skill)
                break
    
    return (len(matched_skills) / len(job_skills)) * 100

def analyze_experience(resume_text):
    doc = nlp(resume_text.lower())
    experience_years = 0
    for ent in doc.ents:
        if ent.label_ == 'DATE':
            try:
                years = w2n.word_to_num(ent.text)
                if 0 < years < 50:  # Reasonable range for work experience
                    experience_years = max(experience_years, years)
            except ValueError:
                continue
    return experience_years

def extract_education(resume_text):
    education_keywords = ['bachelor', 'master', 'phd', 'diploma', 'degree']
    doc = nlp(resume_text.lower())
    education = []
    for sent in doc.sents:
        if any(keyword in sent.text for keyword in education_keywords):
            education.append(sent.text.strip())
    return education

def calculate_ats_score(resume_path, job_description, required_skills, experience_years):
    try:
        resume_text = extract_text(resume_path)
        preprocessed_resume = preprocess_text(resume_text)
        preprocessed_job = preprocess_text(job_description)
        
        resume_skills = extract_skills(preprocessed_resume, required_skills)
        job_skills = set(required_skills)
        
        keyword_score = calculate_keyword_score(preprocessed_resume, preprocessed_job)
        structure_score = analyze_resume_structure(resume_text)
        skill_match_score = calculate_skill_match(resume_skills, job_skills)
        total_experience_years = analyze_experience(resume_text)
        education = extract_education(resume_text)
        
        experience_score = min(total_experience_years / experience_years, 1) * 100 if experience_years > 0 else 100
        
        final_score = (
            keyword_score * 0.3 +
            structure_score * 0.1 +
            skill_match_score * 0.3 +
            experience_score * 0.2 +
            (100 if education else 0) * 0.1
        )
        
        return {
            'final_score': final_score,
            'keyword_score': keyword_score,
            'structure_score': structure_score,
            'skill_match_score': skill_match_score,
            'experience_years': total_experience_years,
            'education': education,
            'resume_skills': list(resume_skills),
            'job_skills': list(job_skills),
            'contact_info': extract_contact_info(resume_text)
        }
    except Exception as e:
        return {
            'error': str(e),
            'final_score': 0,
            'keyword_score': 0,
            'structure_score': 0,
            'skill_match_score': 0,
            'experience_years': 0,
            'education': [],
            'resume_skills': [],
            'job_skills': [],
            'contact_info': {}
        }

def analyze_multiple_resumes(resume_paths, job_description, skills, experience_years):
    download_nltk_resources()
    results = {}
    for resume_path in resume_paths:
        try:
            resume_name = os.path.basename(resume_path)
            scores = calculate_ats_score(resume_path, job_description, skills, experience_years)
            results[resume_name] = scores
        except Exception as e:
            results[resume_name] = {'error': str(e)}
    return results

def save_results_to_csv(results):
    df = pd.DataFrame.from_dict(results, orient='index')
    csv_file_path = "resume_scores.csv"
    df.to_csv(csv_file_path)
    return csv_file_path
