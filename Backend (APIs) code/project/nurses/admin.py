from django.contrib import admin
from .models import City,Governorate,Nurse,Specialty
# Register your models here.
admin.site.register(Governorate)
admin.site.register(City)
admin.site.register(Nurse)
admin.site.register(Specialty)