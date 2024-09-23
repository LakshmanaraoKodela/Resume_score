import PyPDF2
import docx
import nltk
import json

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in range(len(reader.pages)):
        text += reader.pages[page].extract_text()
    return text

def extract_text_from_docx(file):
    doc = docx.Document(file)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

def clean_text(text):
    stop_words = set(nltk.corpus.stopwords.words('english'))
    words = nltk.word_tokenize(text.lower())
    words = [word for word in words if word.isalnum() and word not in stop_words]
    return words

def load_skills_db(file_path):
    with open(file_path, 'r') as file:
        skills_db = json.load(file)
    return skills_db

def calculate_ats_score(resume_text, job_description, skills_db):
    resume_words = clean_text(resume_text)
    job_words = clean_text(job_description)
    
    # Keyword match score
    keyword_matches = len(set(job_words) & set(resume_words))
    keyword_score = keyword_matches / len(set(job_words)) if job_words else 0
    
    # Skill match score
    skill_matches = len(set(skills_db) & set(resume_words))
    skill_match_score = skill_matches / len(skills_db) if skills_db else 0
    
    # Experience (example placeholder logic)
    experience_years = sum(1 for word in resume_words if word.isdigit())  # placeholder for experience parsing
    
    # Final score
    final_score = 0.4 * keyword_score + 0.4 * skill_match_score + 0.2 * min(experience_years / 10, 1)
    
    return {
        "final_score": final_score * 100,
        "keyword_score": keyword_score * 100,
        "skill_match_score": skill_match_score * 100,
        "experience_years": experience_years
    }
