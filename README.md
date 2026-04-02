# 🔍 JobLens — AI Resume Matcher

![JobLens Banner](https://img.shields.io/badge/JobLens-AI%20Resume%20Matcher-2E9AF7?style=for-the-badge)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

> An AI-driven resume analyzer that matches your resume against a job description, identifies skill gaps, and suggests personalized learning resources.

## 🚀 Live Demo
**Frontend:** [https://joblens-frontend-pearl.vercel.app](https://joblens-frontend-pearl.vercel.app)  
**Backend API:** [https://joblens-backend-zbxo.onrender.com](https://joblens-backend-zbxo.onrender.com)

---

## ✨ Features

- 📄 **Resume Parsing** — Extracts text from PDF resumes
- 🧠 **AI Skill Extraction** — Uses NLP (spaCy) to identify skills from resume and job description
- 📊 **Match Scoring** — Calculates how well your resume matches the job
- 🎯 **Skill Gap Analysis** — Shows exactly which skills you're missing
- 📚 **Learning Suggestions** — Recommends YouTube tutorials and Udemy courses for missing skills

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React, Tailwind CSS, Vite |
| Backend | Django, Django REST Framework |
| ML/NLP | spaCy, scikit-learn |
| Resume Parsing | pdfplumber, pdfminer |
| Deployment | Vercel (Frontend), Render (Backend) |

---

## 🏃 Run Locally

### Backend
```bash
git clone https://github.com/hshimaila/JobLens
cd JobLens
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
```

### Frontend
```bash
cd joblens-frontend
npm install
npm run dev
```

---

## 📡 API Usage

**POST** `/api/analyze/`

| Field | Type | Description |
|---|---|---|
| `resume` | File | PDF resume file |
| `job_description` | Text | Job description text |

**Response:**
```json
{
  "match_score": 80.0,
  "matched_skills": ["Python", "Django", "React"],
  "missing_skills": ["Docker"],
  "suggestions": {
    "Docker": {
      "videos": [{"title": "Docker tutorial", "link": "..."}],
      "courses": [{"title": "Docker course", "link": "..."}]
    }
  }
}
```

---

## 👩‍💻 Author

**Shimaila Hanif** 

[GitHub](https://github.com/hshimaila) · [LinkedIn](https://www.linkedin.com/in/shimaila-hanif-08ba1b262/)