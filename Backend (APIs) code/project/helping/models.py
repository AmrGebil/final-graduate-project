from django.db import models

def first_aid_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "first_aid/%s.%s"%(instance.id,extension)

def disease_knowledge_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "disease_knowledge/%s.%s"%(instance.id,extension)


# Create your models here.
class first_aid (models.Model):
    its_photo= models.ImageField(upload_to=first_aid_upload, null=True, blank=True)
    name=models.CharField(max_length=150)
    desciption=models.TextField(max_length=1000)
    treatment=models.TextField(max_length=1000)
    def __str__(self):
        return self.name

class disease_knowledge (models.Model):
    its_photo= models.ImageField(upload_to=disease_knowledge_upload, null=True, blank=True)
    name=models.CharField(max_length=150)
    desciption=models.TextField(max_length=1000)
    treatment=models.TextField(max_length=1000)
    def __str__(self):
        return self.name