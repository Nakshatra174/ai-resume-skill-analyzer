# AI Resume Skill Analyzer

An AI-based tool that analyzes a candidate’s resume and compares it with a job description to calculate a skill match score.

Built using **Python, Streamlit, and NLP-based keyword matching**.

---

## Features

- Upload resume in PDF format
- Extract text automatically
- Detect skills from the resume
- Compare resume skills with job description
- Calculate match score
- Identify missing skills required for the job
- Visual match score progress bar

---

## Technologies Used

- Python
- Streamlit
- pdfplumber
- NLP-based keyword matching

---

## How to Run the Project

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
streamlit run app.py
```

Then open the browser at:

```
http://localhost:8501
```

---

## Project Structure

```
ai-resume-analyzer
│
├── app.py
├── resume_analyzer.py
├── sample_resume.pdf
├── job_description.txt
└── requirements.txt
```

---

## Author

Nakshatra Jeothish