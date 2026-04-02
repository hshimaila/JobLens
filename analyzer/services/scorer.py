from analyzer.services.skill_extractor import SkillExtractor

class JobScorer:
    def analyze(self, resume_text, job_desc):
        extractor = SkillExtractor()

        resume_skills = extractor.extract(resume_text)
        job_skills = extractor.extract(job_desc)

        matched_skills = list(set(resume_skills) & set(job_skills))
        missing_skills = list(set(job_skills) - set(resume_skills))

        if not job_skills:
            match_score = 0.0
        else:
            match_score = (len(matched_skills) / len(job_skills)) * 100

        return {
            "match_score": match_score,
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "resume_skills": resume_skills,
            "job_skills": job_skills,
        }
