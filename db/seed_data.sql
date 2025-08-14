-- Insert users
INSERT INTO users (name, email, password, role) VALUES
('Alice Johnson', 'alice@example.com', 'hashed_password_1', 'JOB_SEEKER'),
('Bob Smith', 'bob@example.com', 'hashed_password_2', 'EMPLOYER'),
('Charlie Admin', 'admin@example.com', 'hashed_password_3', 'ADMIN');

-- Insert jobs
INSERT INTO jobs (title, description, location, company_name, employer_id) VALUES
('Frontend Developer', 'Build responsive web apps using React and Angular.', 'New York, USA', 'TechCorp', 2),
('Backend Developer', 'Develop scalable APIs using Spring Boot.', 'San Francisco, USA', 'CodeWave', 2);

-- Insert applications
INSERT INTO applications (job_id, applicant_id, status) VALUES
(1, 1, 'PENDING'),
(2, 1, 'PENDING');
