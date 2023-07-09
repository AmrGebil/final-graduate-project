from django.urls import path
from . import views
# 'jobs/' the main link
urlpatterns = [
    path('',views.doctorList,name="doctors_list"),
    path('<int:id>',views.doctor_details,name="doctor_details"),
   
]