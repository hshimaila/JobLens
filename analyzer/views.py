from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os
from django.conf import settings
from .services.resume_parser import ResumeParser
from .services.skill_extractor import SkillExtractor
from .services.scorer import JobScorer


@api_view(['POST'])
def analyze_resume(request):
    try:
        # 📥 Get data from request
        resume_file = request.FILES.get("resume")
        job_desc = request.data.get("job_description")

        if not resume_file or not job_desc:
            return Response(
                {"error": "Resume file and job description are required"},
                status=400
            )

        # 💾 Save resume file
        fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'resumes'))
        filename = fs.save(resume_file.name, resume_file)
        file_path = fs.path(filename)

        # 🧠 ML Pipeline
        parser = ResumeParser()
        extractor = SkillExtractor()
        scorer = JobScorer()

        resume_text = parser.extract_text(file_path)

        if not resume_text or not resume_text.strip():
            return Response(
                {"error": "Could not extract text from resume"},
                status=400
            )

        resume_skills = extractor.extract(resume_text)
        job_skills = extractor.extract(job_desc)

        result = scorer.analyze(resume_text, job_desc)

        matched_skills = result.get("matched_skills", [])
        missing_skills = result.get("missing_skills", [])

        # 📚 Suggestions Mapping
        suggestions_map = {
            "Docker": {
                "videos": [
                    {
                        "title": "Docker Crash Course",
                        "link": "https://youtube.com/results?search_query=docker+tutorial"
                    }
                ],
                "courses": [
                    {
                        "title": "Docker for Beginners",
                        "link": "https://www.udemy.com/topic/docker/"
                    }
                ]
            },
            "AWS": {
                "videos": [
                    {
                        "title": "AWS Basics",
                        "link": "https://youtube.com/results?search_query=aws+tutorial"
                    }
                ],
                "courses": [
                    {
                        "title": "AWS Certified Course",
                        "link": "https://www.udemy.com/topic/aws/"
                    }
                ]
            },
            "React": {
                "videos": [
                    {
                        "title": "React Full Course",
                        "link": "https://youtube.com/results?search_query=react+tutorial"
                    }
                ],
                "courses": [
                    {
                        "title": "React for Beginners",
                        "link": "https://www.udemy.com/topic/react/"
                    }
                ]
            }
        }

        # 🔥 Generate Suggestions dynamically
        suggestions = {}

        for skill in missing_skills:
            if skill in suggestions_map:
                suggestions[skill] = suggestions_map[skill]
            else:
                suggestions[skill] = {
                    "videos": [
                        {
                            "title": f"{skill} tutorial",
                            "link": f"https://youtube.com/results?search_query={skill}+tutorial"
                        }
                    ],
                    "courses": [
                        {
                            "title": f"{skill} course",
                            "link": "https://www.udemy.com"
                        }
                    ]
                }

        # 📤 Final Response
        return Response({
            "match_score": round(float(result.get("match_score", 0)), 2),
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "resume_skills": resume_skills,
            "job_skills": job_skills,
            "suggestions": suggestions
        })

    except Exception as e:
        return Response(
            {"error": str(e)},
            status=500
        )