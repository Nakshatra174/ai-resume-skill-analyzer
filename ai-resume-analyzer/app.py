import streamlit as st
import pdfplumber

# Skills list
skills_list = [
    "python", "sql", "machine learning", "data analysis",
    "logistics", "inventory management", "warehouse",
    "supply chain", "mathematics", "cleaning equipment",
    "azure", "networking", "cloud", "docker", "kubernetes"
]

st.title("AI Resume Skill Analyzer")

st.write("Upload a resume and compare it with a job description.")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description")

if st.button("Analyze Resume"):

    if uploaded_file is not None and job_description != "":

        # Extract resume text
        with pdfplumber.open(uploaded_file) as pdf:
            resume_text = ""
            for page in pdf.pages:
                resume_text += page.extract_text()

        resume_text = resume_text.lower()
        job_text = job_description.lower()

        # Detect skills in resume
        resume_skills = []
        for skill in skills_list:
            if skill in resume_text:
                resume_skills.append(skill)

        # Detect skills in job description
        job_skills = []
        for skill in skills_list:
            if skill in job_text:
                job_skills.append(skill)

        # Find matched skills
        matched_skills = []
        for skill in resume_skills:
            if skill in job_skills:
                matched_skills.append(skill)

        # Match score
        if len(job_skills) > 0:
            match_score = (len(matched_skills) / len(job_skills)) * 100
        else:
            match_score = 0

        # Missing skills
        missing_skills = []
        for skill in job_skills:
            if skill not in resume_skills:
                missing_skills.append(skill)

        # Display results
        st.subheader("Analysis Result")

        st.write("Resume Skills Found:")
        st.write(resume_skills)

        st.write("Job Description Skills:")
        st.write(job_skills)

        st.write("Matched Skills:")
        st.write(matched_skills)

        st.write("Missing Skills:")
        st.write(missing_skills)

        st.subheader("Match Score")

        score = round(match_score, 2)

        st.progress(int(score))
        st.success(str(score) + "% match with the job description")

    else:
        st.warning("Please upload a resume and enter a job description.")