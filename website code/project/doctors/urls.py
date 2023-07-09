from django.urls import path
from . import views

urlpatterns = [
    path('',views.doctorList,name="doctors_list"),
    path('<int:id>',views.doctor_details,name="doctor_details"),
   
]