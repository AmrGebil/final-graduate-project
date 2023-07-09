from django.db import models

from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here
def nurse_photo_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "nurse_images/%s.%s"%(instance.id,extension)

 

class Nurse(models.Model):
    the_sex = (
        ('male', 'male'),
        ('female', 'female'))
    his_photo= models.ImageField(upload_to=nurse_photo_upload, null=True, blank=True)
    his_name=models.CharField(max_length=100)
    his_age=models.IntegerField(validators=[
                MinValueValidator(20),
                MaxValueValidator(200)
            ])
    his_sex = models.CharField(max_length=15, choices=the_sex,default="Notfound")
    his_governorate=models.CharField(max_length=100)
    his_city=models.CharField(max_length=100)
    his_specialty=models.CharField(max_length=100)
    his_hospital=models.CharField(max_length=25)
    his_email_for_connect=models.EmailField(default="Notfound")
    his_number_for_connect=models.CharField(max_length=11,default="Notfound")
    his_facebook_account=models.URLField()
    his_instagram_account=models.URLField()
    his_twitter_account=models.URLField()


    def __str__(self):
        if self.his_name == None:
            return "ERROR-CUSTOMER NAME IS NULL"
        return self.his_name
