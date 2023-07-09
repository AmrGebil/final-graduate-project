from django.db import models

# Create your models here.
class first_aid (models.Model):
    name=models.CharField(max_length=150)
    desciption=models.TextField(max_length=1000)
    treatment=models.TextField(max_length=1000)
    def __str__(self):
        return self.name

class disease_knowledge (models.Model):
    name=models.CharField(max_length=150)
    desciption=models.TextField(max_length=1000)
    treatment=models.TextField(max_length=1000)
    def __str__(self):
        return self.name