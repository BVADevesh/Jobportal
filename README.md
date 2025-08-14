<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
</head>
<body>

  <h1>💼 Smart Job Portal with Resume Parsing & Recommendations</h1>
  <p>
    An intelligent job portal system that automatically <strong>parses resumes</strong> to extract candidate skills
    and provides <strong> job recommendations</strong> based on skill matching.  
    Built for job seekers, recruiters, and HR professionals to streamline hiring and application processes.
  </p>

  <h2>📌 Project Overview</h2>
  <p>
    This project combines <strong>Spring Boot</strong> for backend, <strong>HTML/CSS/JS</strong> for frontend, and 
    <strong>Python scripts</strong> for resume parsing and job recommendation logic.  
    It allows candidates to upload resumes, employers to post jobs, and the system to automatically recommend the most relevant roles.
  </p>

  <h2>🛠️ Features</h2>
  <ul>
    <li>📄 Automated PDF/DOCX Resume Parsing</li>
    <li>🤖 Job Recommendations Based on Skills</li>
    <li>🗄️ MySQL Database for Storing Jobs & Candidates</li>
    <li>📊 Employer Dashboard for Job Management</li>
    <li>🌐 REST API Integration</li>
    <li>⚡ Instant Job Posting & Retrieval</li>
  </ul>

  <h2>🧱 Project Structure</h2>
  <pre>
job-portal/
│
├── backend/
│   ├── controller/
│   ├── model/
│   ├── repository/
│   ├── service/
│   ├── JobPortalApplication.java
│
├── resources/
│   ├── application.properties
│   ├── schema.sql
│   ├── seed_data.sql
│
├── frontend/
│   ├── index.html
│   ├── dashboard.html
│   ├── css/
│   ├── js/
│
├── scripts/
│   ├── resume_parser.py
│   ├── job_recommender.py
│
└── README.html
  </pre>

  <h2>🚀 Getting Started</h2>
  <h3>1. Clone the repository</h3>
  <pre><code>
git clone https://github.com/your-username/job-portal.git
cd job-portal
  </code></pre>

  <h3>2. Backend Setup</h3>
  <pre><code>
# Configure database in application.properties
spring.datasource.url=jdbc:mysql://localhost:3306/job_portal
spring.datasource.username=root
spring.datasource.password=yourpassword

# Run backend
mvn spring-boot:run
  </code></pre>

  <h3>3. Python Scripts Setup</h3>
  <pre><code>
pip install spacy docx2txt pdfminer.six scikit-learn pandas
python -m spacy download en_core_web_sm

# Run parsing
python scripts/resume_parser.py sample_resume.pdf
python scripts/job_recommender.py
  </code></pre>

  <h2>💡 Example Workflow</h2>
  <blockquote>
    “A candidate uploads their resume → System extracts skills → System fetches top matching jobs → Recommendations are shown instantly.”
  </blockquote>

  <h2>📦 Dependencies</h2>
  <pre><code>
Spring Boot
MySQL
Lombok
JPA
spacy
pdfminer.six
docx2txt
scikit-learn
pandas
  </code></pre>

  <h2>🤝 Contributing</h2>
  <ol>
    <li>Fork the repo</li>
    <li>Create a new branch (<code>git checkout -b feature/your-feature</code>)</li>
    <li>Make your changes</li>
    <li>Push and create a PR</li>
  </ol>
  
  <hr>

 <h2>🙋‍♂️ Author</h2>
  <p>
    Developed by <strong>Bellamkonda V A Devesh</strong><br>
    For research, collaboration, or freelance inquiries, connect on 
    <a href="https://www.linkedin.com/in/bellamkonda-v-81511a289/" target="_blank">LinkedIn</a>.
  </p>

  <hr>
  <blockquote><em>
    “Your resume deserves the right job — let my JobPortal find it for you.”
  </em></blockquote>

</body>
</html>
