from django.contrib import admin
from .models import UserProfile,MedicalHistory
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(MedicalHistory)
