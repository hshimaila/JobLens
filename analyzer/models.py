from django.db import models


class ResumeUpload(models.Model):
    file = models.FileField(upload_to="resumes/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resume {self.id}"


class AnalysisResult(models.Model):
    resume = models.ForeignKey(
        ResumeUpload,
        on_delete=models.CASCADE,
        related_name="analyses",
        null=True,
        blank=True,
    )

    match_score = models.FloatField()
    matched_skills = models.JSONField()
    missing_skills = models.JSONField()
    resume_skills = models.JSONField()
    job_skills = models.JSONField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Analysis {self.id} - {self.match_score}%"
