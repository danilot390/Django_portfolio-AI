from django.urls import path
from .views import home, about_view, experiences, experience_detail

urlpatterns = [
    path("", home, name="home"),
    path("experiences", experiences, name='experiences'),
    path("experience/<slug:slug>/", experience_detail, name='experience_detail'),
    path("about", about_view, name='about')
]