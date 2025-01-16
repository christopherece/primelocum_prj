from django.contrib import admin
from .models import (
    Profile,
    WorkExperience,
    WorkExperienceDetail,
    Skill,
    Certification,
    Education,
)

# Inline models
class WorkExperienceDetailInline(admin.TabularInline):
    model = WorkExperienceDetail
    extra = 1  # Number of extra empty forms displayed

class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company_name', 'location', 'start_date', 'end_date')
    search_fields = ('job_title', 'company_name', 'location')
    list_filter = ('start_date', 'end_date')
    inlines = [WorkExperienceDetailInline]

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CertificationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'graduation_year')
    search_fields = ('degree', 'institution')
    list_filter = ('graduation_year',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'location', 'short_intro', 'created')
    search_fields = ('name', 'email', 'location')
    list_filter = ('created',)
    filter_horizontal = ('skills', 'certifications', 'work_experiences')  # For ManyToMany fields

# Register models with admin site
admin.site.register(Profile, ProfileAdmin)
admin.site.register(WorkExperience, WorkExperienceAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Certification, CertificationAdmin)
admin.site.register(Education, EducationAdmin)
