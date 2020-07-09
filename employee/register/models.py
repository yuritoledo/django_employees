from django.db import models


class Department(models.Model):
    name = models.TextField(max_length=50)


class Employee(models.Model):
    name = models.TextField(max_length=200)
    email = models.TextField(max_length=50, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
