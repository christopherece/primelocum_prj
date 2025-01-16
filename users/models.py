import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class WorkExperience(models.Model):
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # End date can be null if the job is ongoing
    description = models.TextField()

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"

class WorkExperienceDetail(models.Model):
    work_experience = models.ForeignKey(WorkExperience, related_name='details', on_delete=models.CASCADE)
    task_description = models.TextField()

    def __str__(self):
        return f"Task in {self.work_experience.job_title}"

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Certification(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    graduation_year = models.IntegerField()

    def __str__(self):
        return f"{self.degree} from {self.institution}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=30, blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)
    short_intro = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default="profiles/user-default.png")
    profile_cv = models.FileField(null=True, blank=True, upload_to='cv')
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_youtube = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    skills = models.ManyToManyField(Skill, related_name="profiles", blank=True)
    certifications = models.ManyToManyField(Certification, related_name="profiles", blank=True)
    work_experiences = models.ManyToManyField(WorkExperience, related_name='profiles', blank=True)
    education = models.OneToOneField(Education, on_delete=models.SET_NULL, null=True, blank=True)
    interests = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.user.username) if self.user else self.name
