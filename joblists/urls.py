from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='joblists'),
    path('joblist/<int:job_id>/', views.joblist, name='joblist'),


]