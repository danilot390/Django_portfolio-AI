from django.urls import path
from .views import projects, project_detail

urlpatterns = [
    path("", projects, name="projects"),
    path("<slug:slug>/", project_detail, name="project_detail"),
]