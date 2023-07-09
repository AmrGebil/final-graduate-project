from django.contrib import admin
from .models import City,Governorate,Doctor,Specialty
# Register your models here.
admin.site.register(Governorate)
admin.site.register(City)
admin.site.register(Doctor)
admin.site.register(Specialty)