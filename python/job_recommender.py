# job_recommender.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class JobRecommender:
    def __init__(self, job_data_path):
        """
        Initialize recommender with job data from CSV.
        job_data_path: Path to CSV with columns: id, title, company, skillsRequired, description
        """
        self.jobs_df = pd.read_csv(job_data_path)
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.job_matrix = None
        self._prepare_data()

    def _prepare_data(self):
        """Create TF-IDF matrix for skillsRequired column."""
        self.jobs_df['skillsRequired'] = self.jobs_df['skillsRequired'].fillna('')
        self.job_matrix = self.vectorizer.fit_transform(self.jobs_df['skillsRequired'])

    def recommend_jobs(self, user_skills, top_n=5):
        """
        Recommend jobs based on user skills.
        user_skills: string of comma-separated skills
        """
        user_vector = self.vectorizer.transform([user_skills])
        similarities = cosine_similarity(user_vector, self.job_matrix).flatten()
        top_indices = similarities.argsort()[-top_n:][::-1]
        recommendations = self.jobs_df.iloc[top_indices]
        return recommendations[['id', 'title', 'company', 'skillsRequired', 'description']]


if __name__ == "__main__":
    # Example usage:
    recommender = JobRecommender("jobs.csv")  # CSV file with job data
    skills = input("Enter your skills (comma separated): ")
    recs = recommender.recommend_jobs(skills, top_n=5)

    print("\nTop Recommended Jobs:\n")
    for _, row in recs.iterrows():
        print(f"{row['title']} at {row['company']}")
        print(f"Skills: {row['skillsRequired']}")
        print(f"Description: {row['description'][:100]}...\n")
