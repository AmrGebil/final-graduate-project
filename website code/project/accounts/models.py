from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField( upload_to='profile_images',null=True, blank=True,default='default.png')
    # bio = models.TextField()
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    illnesses_numbers = models.IntegerField(null=True, blank=True)
    illnesses = models.CharField(max_length=30, null=True, blank=True)
    illnesses_descriptions = models.TextField(max_length=600, null=True, blank=True)
    allergies = models.TextField(max_length=150, null=True, blank=True)
    surgeries = models.TextField(max_length=150, null=True, blank=True)
    immunizations = models.TextField(max_length=150, null=True, blank=True)
    results_of_physical_exams_and_tests = models.TextField(max_length=150, null=True, blank=True)
    physical_exams_and_tests_images = models.ImageField(upload_to='medical_images', null=True, blank=True)
    medicines = models.TextField(max_length=150, null=True, blank=True)
    medicines_images = models.ImageField(upload_to='medical_images', null=True, blank=True)
    medical_rays = models.TextField(max_length=150, null=True, blank=True)
    medical_rays_images = models.ImageField(upload_to='medical_images', null=True, blank=True)
    health_habits = models.TextField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)







class MedicalHistory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


