# resume_parser.py
import re
import docx2txt
import spacy
from pdfminer.high_level import extract_text

# Load English NLP model for named entity recognition
nlp = spacy.load("en_core_web_sm")

# Common skills list (expand as needed)
COMMON_SKILLS = [
    "Python", "Java", "C++", "C", "JavaScript", "Spring Boot", "Django", "Flask", "React",
    "Angular", "Node.js", "MySQL", "PostgreSQL", "MongoDB", "AWS", "Azure", "Git", "Docker",
    "Kubernetes", "HTML", "CSS", "Linux", "Cybersecurity", "Machine Learning", "AI", "Data Science"
]

def extract_text_from_file(file_path):
    """Extract text from PDF or DOCX."""
    if file_path.lower().endswith(".pdf"):
        return extract_text(file_path)
    elif file_path.lower().endswith(".docx"):
        return docx2txt.process(file_path)
    else:
        raise ValueError("Unsupported file format. Only PDF and DOCX are supported.")

def extract_skills(text):
    """Extract skills from resume text."""
    found_skills = set()
    for skill in COMMON_SKILLS:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text, re.IGNORECASE):
            found_skills.add(skill)
    return list(found_skills)

def extract_name(text):
    """Extract the most likely candidate name using NLP."""
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

def extract_email(text):
    """Extract email from text."""
    match = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    return match.group(0) if match else None

def extract_phone(text):
    """Extract phone number from text."""
    match = re.search(r"(\+?\d{1,3}[-.\s]?)?\d{10}", text)
    return match.group(0) if match else None

def parse_resume(file_path):
    """Main parser function."""
    text = extract_text_from_file(file_path)
    name = extract_name(text)
    email = extract_email(text)
    phone = extract_phone(text)
    skills = extract_skills(text)

    return {
        "name": name,
        "email": email,
        "phone": phone,
        "skills": skills
    }

if __name__ == "__main__":
    # Example usage
    file_path = "sample_resume.pdf"  # Change to your resume file
    data = parse_resume(file_path)
    
    print("\nExtracted Resume Data:")
    for key, value in data.items():
        print(f"{key}: {value}")
