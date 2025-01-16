from django.contrib import admin

# Register your models here.
from .models import Profile, WorkExperience, WorkExperienceDetail

# Customizing the admin interface for WorkExperienceDetail
class WorkExperienceDetailInline(admin.TabularInline):
    model = WorkExperienceDetail
    extra = 1  # Number of empty forms to display by default

# Customizing the admin interface for WorkExperience
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company_name', 'location', 'start_date', 'end_date')
    search_fields = ('job_title', 'company_name', 'location')
    inlines = [WorkExperienceDetailInline]  # Allow editing WorkExperienceDetails inline

# Customizing the admin interface for Profile
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email', 'location', 'created')
    search_fields = ('user__username', 'name', 'email')
    filter_horizontal = ('work_experiences',)  # Add this to manage the many-to-many relationship in a user-friendly way

    # You can also customize form layout and fieldsets as per your requirements
    fieldsets = (
        (None, {
            'fields': ('user', 'name', 'email', 'location', 'about_me', 'short_intro', 'profile_image', 'profile_cv')
        }),
        ('Social Links', {
            'fields': ('social_linkedin', 'social_twitter', 'social_youtube', 'social_website')
        }),
        ('Work Experience', {
            'fields': ('work_experiences',)
        }),
    )

# Registering models with the admin interface
admin.site.register(Profile, ProfileAdmin)
admin.site.register(WorkExperience, WorkExperienceAdmin)
admin.site.register(WorkExperienceDetail)