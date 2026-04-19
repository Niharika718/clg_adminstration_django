from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    student_class = models.CharField(max_length=50)
    marks = models.IntegerField()


class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    doj = models.DateField()