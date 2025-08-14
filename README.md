<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Job Portal – README</title>
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <meta name="description" content="Job Portal with Resume Parsing & Job Recommendations" />
  <style>
    :root{
      --bg:#0f172a; --card:#0b1220; --muted:#94a3b8; --text:#e2e8f0; --accent:#22d3ee; --accent-2:#a78bfa;
      --border:#1f2937; --chip:#111827; --ok:#10b981; --warn:#f59e0b; --danger:#ef4444;
    }
    *{box-sizing:border-box}
    body{margin:0;background:var(--bg);color:var(--text);font:16px/1.6 system-ui,-apple-system,Segoe UI,Roboto,Ubuntu,"Helvetica Neue",Arial}
    a{color:var(--accent)}
    .container{max-width:1100px;margin:0 auto;padding:24px}
    header{position:sticky;top:0;background:rgba(15,23,42,.9);backdrop-filter:saturate(150%) blur(6px);border-bottom:1px solid var(--border);z-index:10}
    header .inner{display:flex;align-items:center;justify-content:space-between;padding:14px 24px}
    h1{font-size:28px;margin:0}
    .badge{padding:3px 8px;border:1px solid var(--border);border-radius:10px;font-size:12px;color:var(--muted)}
    .grid{display:grid;gap:16px}
    @media(min-width:900px){ .grid-2{grid-template-columns:1fr 1fr} .grid-3{grid-template-columns:repeat(3,1fr)} }
    section{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:22px}
    h2{margin:0 0 10px;font-size:22px}
    h3{margin:16px 0 8px;font-size:18px}
    .list{margin:10px 0 0 0;padding-left:18px}
    .kvs{display:grid;gap:8px}
    .kvs div{display:flex;gap:10px}
    .chip{display:inline-flex;align-items:center;gap:6px;padding:6px 10px;border:1px solid var(--border);border-radius:999px;background:var(--chip);font-size:13px;color:var(--muted)}
    code,pre{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;background:#0a0f1a;border:1px solid var(--border);border-radius:10px}
    pre{padding:14px;overflow:auto}
    .img-wrap{border:1px dashed var(--border);border-radius:12px;display:flex;align-items:center;justify-content:center;min-height:180px;background:#0a0f1a}
    .img-wrap img{max-width:100%;border-radius:10px}
    .pill{padding:2px 8px;border-radius:999px;background:#0a0f1a;border:1px solid var(--border);color:var(--muted);font-size:12px}
    .table{width:100%;border-collapse:collapse;border:1px solid var(--border);border-radius:10px;overflow:hidden}
    .table th,.table td{border-bottom:1px solid var(--border);padding:10px;text-align:left}
    .flex{display:flex;gap:8px;flex-wrap:wrap}
    footer{color:var(--muted);padding:24px 0;text-align:center}
  </style>
  <!-- Mermaid for the workflow diagram -->
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
  <script>mermaid.initialize({ startOnLoad: true, theme: "dark" });</script>
</head>
<body>
  <header>
    <div class="inner container">
      <h1>🚀 Job Portal with Resume Parsing & Job Recommendations</h1>
      <span class="badge">README · HTML</span>
    </div>
  </header>

  <main class="container grid grid-2">
    <!-- Overview -->
    <section>
      <h2>📌 Overview</h2>
      <p>
        A smart job portal that <strong>parses resumes</strong> (PDF/DOCX) to extract candidate details and
        <strong>recommends jobs</strong> based on skills. Includes a clean web UI and a Spring Boot backend.
      </p>
      <div class="flex">
        <span class="chip">Spring Boot</span>
        <span class="chip">MySQL</span>
        <span class="chip">HTML/CSS/JS</span>
        <span class="chip">Python</span>
        <span class="chip">spaCy</span>
        <span class="chip">scikit-learn</span>
      </div>
    </section>

    <!-- Features -->
    <section>
      <h2>✨ Features</h2>
      <ul class="list">
        <li><strong>Resume Parser:</strong> Name, Email, Phone, Skills • PDF & DOCX.</li>
        <li><strong>Job Recommender:</strong> TF-IDF + cosine similarity for skill match.</li>
        <li><strong>Web Dashboard:</strong> Post jobs & view recommendations.</li>
        <li><strong>Database:</strong> Schema + seed data included.</li>
      </ul>
    </section>

    <!-- Screenshots -->
    <section>
      <h2>🖼️ Screenshots</h2>
      <div class="grid grid-2">
        <div>
          <h3>Home Page</h3>
          <div class="img-wrap">
            <!-- Replace with your actual image path -->
            <img src="assets/home_screenshot.png" alt="Home screenshot" onerror="this.parentElement.innerHTML='Add assets/home_screenshot.png';">
          </div>
        </div>
        <div>
          <h3>Dashboard</h3>
          <div class="img-wrap">
            <img src="assets/dashboard_screenshot.png" alt="Dashboard screenshot" onerror="this.parentElement.innerHTML='Add assets/dashboard_screenshot.png';">
          </div>
        </div>
        <div>
          <h3>Recommendations</h3>
          <div class="img-wrap">
            <img src="assets/job_recommendations.png" alt="Recommendations screenshot" onerror="this.parentElement.innerHTML='Add assets/job_recommendations.png';">
          </div>
        </div>
        <div>
          <h3>Banner</h3>
          <div class="img-wrap">
            <img src="assets/banner.png" alt="Project banner" onerror="this.parentElement.innerHTML='Add assets/banner.png';">
          </div>
        </div>
      </div>
    </section>

    <!-- Workflow Diagram -->
    <section>
      <h2>📊 Workflow</h2>
      <div class="mermaid">
        flowchart LR
          A[Candidate Uploads Resume] --> B[Resume Parser (Python)]
          B --> C[Extracted Skills]
          C --> D[Job Recommender (Python)]
          D --> E[Match Jobs in MySQL]
          E --> F[Spring Boot API]
          F --> G[Web UI Shows Recommendations]
      </div>
    </section>

    <!-- Tech Stack -->
    <section>
      <h2>🛠️ Tech Stack</h2>
      <table class="table">
        <tr><th>Layer</th><th>Technology</th></tr>
        <tr><td>Backend</td><td>Spring Boot, Java, JPA</td></tr>
        <tr><td>Frontend</td><td>HTML, CSS, JavaScript</td></tr>
        <tr><td>Scripts</td><td>Python (resume_parser, job_recommender)</td></tr>
        <tr><td>Database</td><td>MySQL</td></tr>
        <tr><td>ML</td><td>spaCy, scikit-learn</td></tr>
      </table>
    </section>

    <!-- Project Structure -->
    <section>
      <h2>📂 Project Structure</h2>
      <pre><code>project-root/
├─ backend/ (Spring Boot)
│  ├─ src/main/java/com/jobportal/...
│  └─ src/main/resources/
│     ├─ application.properties
│     ├─ schema.sql
│     └─ seed_data.sql
├─ frontend/
│  ├─ index.html
│  ├─ dashboard.html
│  ├─ css/styles.css
│  └─ js/main.js
├─ python/
│  ├─ resume_parser.py
│  └─ job_recommender.py
├─ assets/ (images used by README.html)
└─ README.html
</code></pre>
    </section>

    <!-- Setup -->
    <section>
      <h2>⚙️ Setup</h2>
      <h3>1) Clone</h3>
      <pre><code>git clone https://github.com/your-username/job-portal.git
cd job-portal</code></pre>

      <h3>2) Python deps</h3>
      <pre><code>pip install spacy docx2txt pdfminer.six scikit-learn pandas
python -m spacy download en_core_web_sm</code></pre>

      <h3>3) MySQL</h3>
      <pre><code>CREATE DATABASE job_portal;</code></pre>
      <pre><code>mysql -u root -p job_portal &lt; backend/src/main/resources/schema.sql
mysql -u root -p job_portal &lt; backend/src/main/resources/seed_data.sql</code></pre>

      <h3>4) Spring Boot config</h3>
      <pre><code>spring.datasource.url=jdbc:mysql://localhost:3306/job_portal
spring.datasource.username=root
spring.datasource.password=yourpassword
spring.jpa.hibernate.ddl-auto=update</code></pre>

      <h3>5) Run backend</h3>
      <pre><code>cd backend
mvn spring-boot:run</code></pre>

      <h3>6) Test scripts</h3>
      <pre><code>python python/resume_parser.py sample_resume.pdf
python python/job_recommender.py</code></pre>
    </section>

    <!-- Roadmap -->
    <section>
      <h2>🚀 Roadmap</h2>
      <ul class="list">
        <li>LLM-assisted skill extraction.</li>
        <li>Multi-language parsing.</li>
        <li>Email alerts for matches.</li>
        <li>Responsive, mobile-first UI.</li>
      </ul>
    </section>

    <!-- License & Contact -->
    <section>
      <h2>📜 License & Contact</h2>
      <div class="kvs">
        <div><strong>License:</strong>&nbsp;<span class="pill">MIT</span></div>
        <div><strong>Email:</strong>&nbsp;<a href="mailto:your.email@example.com">your.email@example.com</a></div>
        <div><strong>Portfolio:</strong>&nbsp;<a href="https://your-portfolio-link.com" target="_blank" rel="noreferrer">your-portfolio-link.com</a></div>
      </div>
    </section>
  </main>

  <footer>
    Built with ❤️ for developers & recruiters.
  </footer>
</body>
</html>
