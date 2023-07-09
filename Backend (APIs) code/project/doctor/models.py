from django.db import models

from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here
def doctor_photo_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "doctor_images/%s.%s"%(instance.id,extension)


class Specialty(models.Model):
    name=models.CharField(max_length=15)
    description=models.TextField(max_length=150)
    def __str__(self):
        return self.name


class Governorate(models.Model):
    name=models.CharField(max_length=15)
    def __str__(self):
        return self.name
class City(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class Doctor(models.Model):
    the_sex = (
        ('ذكر', 'ذكر'),
        ('انثي', 'انثي'))
    his_photo= models.ImageField(upload_to=doctor_photo_upload, null=True, blank=True)
    his_name=models.CharField(max_length=100)
    his_age=models.IntegerField(validators=[MinValueValidator(25),MaxValueValidator(200)])
    his_sex=models.CharField( max_length=15,choices=the_sex,default="Notfound")
    his_governorate=models.ForeignKey(Governorate,on_delete=models.CASCADE)
    his_city=models.ForeignKey(City,on_delete=models.CASCADE)
    his_specialty=models.ForeignKey(Specialty,on_delete=models.CASCADE)
    his_clinic_name=models.CharField(max_length=15)
    his_clinic_location=models.CharField(max_length=100)
    his_clinic_number=models.CharField(max_length=11)
    his_clinic_start_at = models.IntegerField(validators=[ MinValueValidator(0),MaxValueValidator(24)])
    his_clinic_finsh_at = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(24)])
    his_clinic_price=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5000)])
    his_email_for_connect=models.EmailField(default="Notfound")
    his_number_for_connect=models.CharField(max_length=11,default="Notfound")

    def __str__(self):
        if self.his_name == None:
            return "ERROR-CUSTOMER NAME IS NULL"
        return self.his_name

