from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def image_ray_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "x_ray_images/%s.%s"%(instance.id,extension)
def image_tests_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "tests_images/%s.%s"%(instance.id,extension)
def image_medicine_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "medicine_images/%s.%s"%(instance.id,extension)

def user_image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "user_images/%s.%s"%(instance.id,extension)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    your_photo = models.ImageField(upload_to=user_image_upload, null=True, blank=True)
    first_name = models.CharField(max_length=30,null=True,blank=True)
    last_name = models.CharField(max_length=30,null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    phone_number = models.CharField(max_length=15,null=True,blank=True)



    def __str__(self):
        return f'{self.user.username} Profile'

class MedicalHistory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='MedicalHistory_of_user')
    illnesses_numbers = models.IntegerField(null=True,blank=True)
    illnesses = models.CharField(max_length=30,null=True,blank=True)
    illnesses_descriptions= models.TextField(max_length=600 ,null=True,blank=True)
    allergies= models.TextField(max_length=150 ,null=True,blank=True)
    surgeries= models.TextField(max_length=150 ,null=True,blank=True)
    immunizations= models.TextField(max_length=150 ,null=True,blank=True)
    results_of_physical_exams_and_tests=models.TextField(max_length=150 ,null=True,blank=True)
    physical_exams_and_tests_images =models.ImageField(upload_to=image_tests_upload,null=True,blank=True)
    medicines=models.TextField(max_length=150 ,null=True,blank=True)
    medicines_images =models.ImageField(upload_to=image_medicine_upload,null=True,blank=True)
    medical_rays = models.TextField(max_length=150, null=True, blank=True)
    medical_rays_images = models.ImageField(upload_to=image_ray_upload, null=True, blank=True)
    health_habits=models.TextField(max_length=150, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} MedicalHistory'
