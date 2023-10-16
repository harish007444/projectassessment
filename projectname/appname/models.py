# appname/models.py
from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField('Student')

class Student(models.Model):
    name = models.CharField(max_length=100)
    teachers = models.ManyToManyField('Teacher')

class Certificate(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    certificate_file = models.FileField(upload_to='certificates/')
