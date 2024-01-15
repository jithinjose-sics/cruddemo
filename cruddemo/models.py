from django.db import models

class student(models.Model):
    name=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

    