from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile
from .models import Profile, Skill, Certification, WorkExperience, Education



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name',
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name', 'email', 'username', 'about_me', 'short_intro', 'location', 'phone',
            'profile_image', 'profile_cv', 'social_linkedin', 'social_twitter', 
            'social_youtube', 'social_website', 'skills', 'certifications', 
            'work_experiences', 'education', 'interests'
        ]
        widgets = {
            'skills': forms.TextInput(attrs={'placeholder': 'Enter skills separated by commas'}),
            'certifications': forms.TextInput(attrs={'placeholder': 'Enter certifications separated by commas'}),
            'work_experiences': forms.TextInput(attrs={'placeholder': 'Enter work experiences separated by commas'}),
            'education': forms.TextInput(attrs={'placeholder': 'Enter education information'}),
            'about_me': forms.Textarea(attrs={'rows': 4}),
            'interests': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_skills(self):
        skills_input = self.cleaned_data['skills']
        # Convert the comma-separated string to a list of Skill objects
        skill_names = [name.strip() for name in skills_input.split(',')]
        skills = Skill.objects.filter(name__in=skill_names)
        return skills

    def clean_certifications(self):
        certifications_input = self.cleaned_data['certifications']
        # Convert the comma-separated string to a list of Certification objects
        certification_names = [name.strip() for name in certifications_input.split(',')]
        certifications = Certification.objects.filter(name__in=certification_names)
        return certifications

    def clean_work_experiences(self):
        work_experience_input = self.cleaned_data['work_experiences']
        # Convert the comma-separated string to a list of WorkExperience objects
        work_experience_titles = [title.strip() for title in work_experience_input.split(',')]
        work_experiences = WorkExperience.objects.filter(job_title__in=work_experience_titles)
        return work_experiences

    def clean_education(self):
        education_input = self.cleaned_data['education']
        # Assuming 'education' is a string to match with the institution or degree
        # Customize this as per your model's requirement
        try:
            education = Education.objects.get(degree__icontains=education_input)
        except Education.DoesNotExist:
            education = None
        return education