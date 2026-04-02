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
                "videos": [{"title": "Docker Crash Course", "link": "https://youtube.com/results?search_query=docker+tutorial+for+beginners"}],
                "courses": [{"title": "Docker for Beginners", "link": "https://www.udemy.com/topic/docker/"}]
            },
            "AWS": {
                "videos": [{"title": "AWS Full Course", "link": "https://youtube.com/results?search_query=aws+tutorial+for+beginners"}],
                "courses": [{"title": "AWS Certified Solutions Architect", "link": "https://www.udemy.com/topic/aws/"}]
            },
            "React": {
                "videos": [{"title": "React Full Course", "link": "https://youtube.com/results?search_query=react+full+course"}],
                "courses": [{"title": "React for Beginners", "link": "https://www.udemy.com/topic/react/"}]
            },
            "Django": {
                "videos": [{"title": "Django Full Course", "link": "https://youtube.com/results?search_query=django+full+course"}],
                "courses": [{"title": "Django & Python", "link": "https://www.udemy.com/topic/django/"}]
            },
            "Python": {
                "videos": [{"title": "Python Full Course", "link": "https://youtube.com/results?search_query=python+full+course+beginners"}],
                "courses": [{"title": "Complete Python Bootcamp", "link": "https://www.udemy.com/topic/python/"}]
            },
            "JavaScript": {
                "videos": [{"title": "JavaScript Full Course", "link": "https://youtube.com/results?search_query=javascript+full+course"}],
                "courses": [{"title": "JavaScript Bootcamp", "link": "https://www.udemy.com/topic/javascript/"}]
            },
            "TypeScript": {
                "videos": [{"title": "TypeScript Tutorial", "link": "https://youtube.com/results?search_query=typescript+tutorial+for+beginners"}],
                "courses": [{"title": "Understanding TypeScript", "link": "https://www.udemy.com/topic/typescript/"}]
            },
            "Node.js": {
                "videos": [{"title": "Node.js Full Course", "link": "https://youtube.com/results?search_query=nodejs+full+course"}],
                "courses": [{"title": "Node.js Developer Course", "link": "https://www.udemy.com/topic/nodejs/"}]
            },
            "REST APIs": {
                "videos": [{"title": "REST API Full Course", "link": "https://youtube.com/results?search_query=rest+api+tutorial"}],
                "courses": [{"title": "REST API Design", "link": "https://www.udemy.com/topic/rest-api/"}]
            },
            "GraphQL": {
                "videos": [{"title": "GraphQL Full Course", "link": "https://youtube.com/results?search_query=graphql+tutorial+for+beginners"}],
                "courses": [{"title": "GraphQL with React", "link": "https://www.udemy.com/topic/graphql/"}]
            },
            "PostgreSQL": {
                "videos": [{"title": "PostgreSQL Tutorial", "link": "https://youtube.com/results?search_query=postgresql+tutorial+for+beginners"}],
                "courses": [{"title": "SQL & PostgreSQL", "link": "https://www.udemy.com/topic/postgresql/"}]
            },
            "MongoDB": {
                "videos": [{"title": "MongoDB Full Course", "link": "https://youtube.com/results?search_query=mongodb+full+course"}],
                "courses": [{"title": "MongoDB Bootcamp", "link": "https://www.udemy.com/topic/mongodb/"}]
            },
            "MySQL": {
                "videos": [{"title": "MySQL Full Course", "link": "https://youtube.com/results?search_query=mysql+full+course"}],
                "courses": [{"title": "MySQL Bootcamp", "link": "https://www.udemy.com/topic/mysql/"}]
            },
            "Redis": {
                "videos": [{"title": "Redis Crash Course", "link": "https://youtube.com/results?search_query=redis+crash+course"}],
                "courses": [{"title": "Redis Bootcamp", "link": "https://www.udemy.com/topic/redis/"}]
            },
            "Kubernetes": {
                "videos": [{"title": "Kubernetes Tutorial", "link": "https://youtube.com/results?search_query=kubernetes+tutorial+for+beginners"}],
                "courses": [{"title": "Kubernetes for Beginners", "link": "https://www.udemy.com/topic/kubernetes/"}]
            },
            "Git": {
                "videos": [{"title": "Git & GitHub Full Course", "link": "https://youtube.com/results?search_query=git+github+full+course"}],
                "courses": [{"title": "Git Complete", "link": "https://www.udemy.com/topic/git/"}]
            },
            "Linux": {
                "videos": [{"title": "Linux Full Course", "link": "https://youtube.com/results?search_query=linux+full+course+for+beginners"}],
                "courses": [{"title": "Linux Command Line Basics", "link": "https://www.udemy.com/topic/linux/"}]
            },
            "Machine Learning": {
                "videos": [{"title": "Machine Learning Full Course", "link": "https://youtube.com/results?search_query=machine+learning+full+course"}],
                "courses": [{"title": "ML A-Z", "link": "https://www.udemy.com/topic/machine-learning/"}]
            },
            "Deep Learning": {
                "videos": [{"title": "Deep Learning Full Course", "link": "https://youtube.com/results?search_query=deep+learning+full+course"}],
                "courses": [{"title": "Deep Learning A-Z", "link": "https://www.udemy.com/topic/deep-learning/"}]
            },
            "TensorFlow": {
                "videos": [{"title": "TensorFlow Tutorial", "link": "https://youtube.com/results?search_query=tensorflow+tutorial+for+beginners"}],
                "courses": [{"title": "TensorFlow Developer", "link": "https://www.udemy.com/topic/tensorflow/"}]
            },
            "CI/CD": {
                "videos": [{"title": "CI/CD Pipeline Tutorial", "link": "https://youtube.com/results?search_query=cicd+pipeline+tutorial"}],
                "courses": [{"title": "CI/CD with GitHub Actions", "link": "https://www.udemy.com/topic/github-actions/"}]
            },
            "System Design": {
                "videos": [{"title": "System Design Full Course", "link": "https://youtube.com/results?search_query=system+design+interview+course"}],
                "courses": [{"title": "Grokking System Design", "link": "https://www.educative.io/courses/grokking-the-system-design-interview"}]
            },
            "Data Structures": {
                "videos": [{"title": "DSA Full Course", "link": "https://youtube.com/results?search_query=data+structures+algorithms+full+course"}],
                "courses": [{"title": "Master DSA", "link": "https://www.udemy.com/topic/data-structures/"}]
            },
            "Vue.js": {
                "videos": [{"title": "Vue.js Full Course", "link": "https://youtube.com/results?search_query=vuejs+full+course"}],
                "courses": [{"title": "Vue.js Bootcamp", "link": "https://www.udemy.com/topic/vue-js/"}]
            },
            "Flutter": {
                "videos": [{"title": "Flutter Full Course", "link": "https://youtube.com/results?search_query=flutter+full+course"}],
                "courses": [{"title": "Flutter Bootcamp", "link": "https://www.udemy.com/topic/flutter/"}]
            },
            "Swift": {
                "videos": [{"title": "Swift Full Course", "link": "https://youtube.com/results?search_query=swift+full+course"}],
                "courses": [{"title": "Swift Programming", "link": "https://www.udemy.com/topic/swift/"}]
            },
            "Kotlin": {
                "videos": [{"title": "Kotlin Full Course", "link": "https://youtube.com/results?search_query=kotlin+full+course"}],
                "courses": [{"title": "Kotlin for Beginners", "link": "https://www.udemy.com/topic/kotlin/"}]
            },
            "Angular": {
                "videos": [{"title": "Angular Full Course", "link": "https://youtube.com/results?search_query=angular+full+course"}],
                "courses": [{"title": "Angular - The Complete Guide", "link": "https://www.udemy.com/topic/angular/"}]
            },
            "Selenium": {
                "videos": [{"title": "Selenium Full Course", "link": "https://youtube.com/results?search_query=selenium+full+course"}],
                "courses": [{"title": "Selenium WebDriver", "link": "https://www.udemy.com/topic/selenium/"}]
            },
            "Jenkins": {
                "videos": [{"title": "Jenkins Tutorial", "link": "https://youtube.com/results?search_query=jenkins+tutorial+for+beginners"}],
                "courses": [{"title": "Jenkins for Beginners", "link": "https://www.udemy.com/topic/jenkins/"}]
            },
            "Ansible": {
                "videos": [{"title": "Ansible Full Course", "link": "https://youtube.com/results?search_query=ansible+full+course"}],
                "courses": [{"title": "Ansible for Beginners", "link": "https://www.udemy.com/topic/ansible/"}]
            },
            "Terraform": {
                "videos": [{"title": "Terraform Full Course", "link": "https://youtube.com/results?search_query=terraform+full+course"}],
                "courses": [{"title": "Terraform for Beginners", "link": "https://www.udemy.com/topic/terraform/"}]
            },
            "PowerShell": {
                "videos": [{"title": "PowerShell Full Course", "link": "https://youtube.com/results?search_query=powershell+full+course"}],
                "courses": [{"title": "PowerShell for Beginners", "link": "https://www.udemy.com/topic/powershell/"}]
            },
            "Go": {
                "videos": [{"title": "Go Programming Full Course", "link": "https://youtube.com/results?search_query=go+programming+full+course"}],
                "courses": [{"title": "Go Programming Bootcamp", "link": "https://www.udemy.com/topic/go/"}]
            },
            "Rust": {
                "videos": [{"title": "Rust Programming Full Course", "link": "https://youtube.com/results?search_query=rust+programming+full+course"}],
                "courses": [{"title": "Rust Programming Bootcamp", "link": "https://www.udemy.com/topic/rust/"}]
            },
            "Scala": {
                "videos": [{"title": "Scala Full Course", "link": "https://youtube.com/results?search_query=scala+full+course"}],
                "courses": [{"title": "Scala for Beginners", "link": "https://www.udemy.com/topic/scala/"}]
            },
            "Hadoop": {
                "videos": [{"title": "Hadoop Full Course", "link": "https://youtube.com/results?search_query=hadoop+full+course"}],
                "courses": [{"title": "Hadoop for Beginners", "link": "https://www.udemy.com/topic/hadoop/"}]
            },
            "Spark": {
                "videos": [{"title": "Apache Spark Full Course", "link": "https://youtube.com/results?search_query=apache+spark+full+course"}],
                "courses": [{"title": "Apache Spark with Scala", "link": "https://www.udemy.com/topic/apache-spark/"}]
            },
            "Elasticsearch": {
                "videos": [{"title": "Elasticsearch Full Course", "link": "https://youtube.com/results?search_query=elasticsearch+full+course"}],
                "courses": [{"title": "Elasticsearch for Beginners", "link": "https://www.udemy.com/topic/elasticsearch/"}]
            },
            "Kafka": {
                "videos": [{"title": "Kafka Full Course", "link": "https://youtube.com/results?search_query=kafka+full+course"}],
                "courses": [{"title": "Kafka for Beginners", "link": "https://www.udemy.com/topic/apache-kafka/"}]
            },
            "RabbitMQ": {
                "videos": [{"title": "RabbitMQ Full Course", "link": "https://youtube.com/results?search_query=rabbitmq+full+course"}],
                "courses": [{"title": "RabbitMQ for Beginners", "link": "https://www.udemy.com/topic/rabbitmq/"}]
            },
            "Microservices": {
                "videos": [{"title": "Microservices Full Course", "link": "https://youtube.com/results?search_query=microservices+full+course"}],
                "courses": [{"title": "Microservices with Spring Boot", "link": "https://www.udemy.com/topic/microservices/"}]
            },
            "Serverless": {
                "videos": [{"title": "Serverless Full Course", "link": "https://youtube.com/results?search_query=serverless+full+course"}],
                "courses": [{"title": "Serverless Framework", "link": "https://www.udemy.com/topic/serverless/"}]
            },
            "DevOps": {
                "videos": [{"title": "DevOps Full Course", "link": "https://youtube.com/results?search_query=devops+full+course"}],
                "courses": [{"title": "DevOps Engineer Course", "link": "https://www.udemy.com/topic/devops/"}]
            },
            "Data Analysis": {
                "videos": [{"title": "Data Analysis Full Course", "link": "https://youtube.com/results?search_query=data+analysis+full+course"}],
                "courses": [{"title": "Data Analysis with Python", "link": "https://www.udemy.com/topic/data-analysis/"}]
            },
            "Data Visualization": {
                "videos": [{"title": "Data Visualization Full Course", "link": "https://youtube.com/results?search_query=data+visualization+full+course"}],
                "courses": [{"title": "Data Visualization with Python", "link": "https://www.udemy.com/topic/data-visualization/"}]
            },
            "Big Data": {
                "videos": [{"title": "Big Data Full Course", "link": "https://youtube.com/results?search_query=big+data+full+course"}],
                "courses": [{"title": "Big Data with Hadoop", "link": "https://www.udemy.com/topic/big-data/"}]
            },
            "Cloud Computing": {
                "videos": [{"title": "Cloud Computing Full Course", "link": "https://youtube.com/results?search_query=cloud+computing+full+course"}],
                "courses": [{"title": "Cloud Computing with AWS", "link": "https://www.udemy.com/topic/cloud-computing/"}]
            },
            "Cybersecurity": {
                "videos": [{"title": "Cybersecurity Full Course", "link": "https://youtube.com/results?search_query=cybersecurity+full+course"}],
                "courses": [{"title": "Cybersecurity for Beginners", "link": "https://www.udemy.com/topic/cyber-security/"}]
            },
            "Blockchain": {
                "videos": [{"title": "Blockchain Full Course", "link": "https://youtube.com/results?search_query=blockchain+full+course"}],
                "courses": [{"title": "Blockchain Developer Course", "link": "https://www.udemy.com/topic/blockchain/"}]
            },
            "AI": {
                "videos": [{"title": "Artificial Intelligence Full Course", "link": "https://youtube.com/results?search_query=artificial+intelligence+full+course"}],
                "courses": [{"title": "AI for Everyone", "link": "https://www.udemy.com/topic/artificial-intelligence/"}]
            },
            "NLP": {
                "videos": [{"title": "NLP Full Course", "link": "https://youtube.com/results?search_query=nlp+full+course"}],
                "courses": [{"title": "Natural Language Processing with Python", "link": "https://www.udemy.com/topic/natural-language-processing/"}]
            },
            "Computer Vision": {
                "videos": [{"title": "Computer Vision Full Course", "link": "https://youtube.com/results?search_query=computer+vision+full+course"}],
                "courses": [{"title": "Computer Vision with Python", "link": "https://www.udemy.com/topic/computer-vision/"}]
            },
            "Reinforcement Learning": {
                "videos": [{"title": "Reinforcement Learning Full Course", "link": "https://youtube.com/results?search_query=reinforcement+learning+full+course"}],
                "courses": [{"title": "Reinforcement Learning with Python", "link": "https://www.udemy.com/topic/reinforcement-learning/"}]
            },
            "Data Engineering": {
                "videos": [{"title": "Data Engineering Full Course", "link": "https://youtube.com/results?search_query=data+engineering+full+course"}],
                "courses": [{"title": "Data Engineering with Python", "link": "https://www.udemy.com/topic/data-engineering/"}]
            },
            "Data Science": {
                "videos": [{"title": "Data Science Full Course", "link": "https://youtube.com/results?search_query=data+science+full+course"}],
                "courses": [{"title": "Data Science A-Z", "link": "https://www.udemy.com/topic/data-science/"}]
            },
            
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