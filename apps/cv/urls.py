from django.urls import path
from .views import cv_print_view, cv_download_view

urlpatterns = [
    path('print/', cv_print_view, name='cv_print'),
    path('download/', cv_download_view, name='cv_download'),
]