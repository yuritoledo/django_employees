from django.db import models


class Department(models.Model):
    name = models.Field(max_length=30)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.TextField(max_length=200)
    email = models.TextField(max_length=50, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
