# appname/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('generate-certificate/<int:teacher_id>/<int:student_id>/', views.generate_certificate, name='generate_certificate'),
    path('verify-certificate/<str:token>/', views.verify_certificate, name='verify_certificate'),
    # Add more URL patterns as needed
]
