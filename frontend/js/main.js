const API_BASE = 'http://localhost:8080/api';

async function fetchJobs() {
  const container = document.getElementById('jobs');
  if (!container) return;

  container.innerHTML = `<p>Loading jobs...</p>`;

  try {
    const res = await fetch(`${API_BASE}/jobs`);
    if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
    const jobs = await res.json();

    if (!jobs.length) {
      container.innerHTML = `<p>No jobs found.</p>`;
      return;
    }

    container.innerHTML = jobs.map(j => `
      <div class="job-card">
        <h3>${j.title} @ ${j.company || 'Unknown Company'}</h3>
        <p>${j.description || 'No description available'}</p>
        <small>${j.location || 'Location not specified'} • ${j.skillsRequired || 'Skills not specified'}</small>
      </div>
    `).join('');
  } catch (err) {
    console.error('Error fetching jobs:', err);
    container.innerHTML = `<p style="color:red;">Failed to load jobs. Please try again later.</p>`;
  }
}

async function createJob(e) {
  e.preventDefault();
  const form = e.target;
  const submitBtn = form.querySelector('button[type="submit"]');
  submitBtn.disabled = true;
  submitBtn.textContent = 'Saving...';

  const payload = {
    title: document.getElementById('title').value.trim(),
    company: document.getElementById('company').value.trim(),
    location: document.getElementById('location').value.trim(),
    skillsRequired: document.getElementById('skillsRequired').value.trim(),
    description: document.getElementById('description').value.trim()
  };

  try {
    const res = await fetch(`${API_BASE}/jobs`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
    form.reset();
    fetchJobs();
  } catch (err) {
    console.error('Error creating job:', err);
    alert('Failed to create job. Please try again.');
  } finally {
    submitBtn.disabled = false;
    submitBtn.textContent = 'Post Job';
  }
}

window.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('jobForm');
  if (form) form.addEventListener('submit', createJob);
  fetchJobs();
});
