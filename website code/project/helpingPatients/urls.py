from django.urls import path
from . import views

# 'jobs/' the main link
urlpatterns = [
    path('fristaid/', views.first_aidView, name="fristAid"),
    path('diseaseknowledge/', views.disease_knowledgeView, name="diseaseKnowledge"),

]