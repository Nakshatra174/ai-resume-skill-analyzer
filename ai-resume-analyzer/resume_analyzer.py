import pdfplumber

# Skills we want to detect
skills_list = [
    "python", "sql", "machine learning", "data analysis",
    "logistics", "inventory management", "warehouse",
    "supply chain", "mathematics", "cleaning equipment"
]

# ---------------- READ RESUME ----------------
with pdfplumber.open("sample_resume.pdf") as pdf:
    resume_text = ""

    for page in pdf.pages:
        resume_text += page.extract_text()

resume_text = resume_text.lower()

# Detect skills in resume
resume_skills = []

for skill in skills_list:
    if skill in resume_text:
        resume_skills.append(skill)

# ---------------- READ JOB DESCRIPTION ----------------
with open("job_description.txt", "r") as file:
    job_text = file.read().lower()

job_skills = []

for skill in skills_list:
    if skill in job_text:
        job_skills.append(skill)

# ---------------- CALCULATE MATCH ----------------
matched_skills = []

for skill in resume_skills:
    if skill in job_skills:
        matched_skills.append(skill)

if len(job_skills) > 0:
    match_score = (len(matched_skills) / len(job_skills)) * 100
else:
    match_score = 0

# ---------------- OUTPUT ----------------
print("\nResume Skills Found:")
print(resume_skills)

print("\nJob Description Skills:")
print(job_skills)

print("\nMatched Skills:")
print(matched_skills)

print("\nMatch Score:")
print(str(round(match_score, 2)) + "%")

# ---------------- FIND MISSING SKILLS ----------------
missing_skills = []

for skill in job_skills:
    if skill not in resume_skills:
        missing_skills.append(skill)

print("\nMissing Skills:")
print(missing_skills)