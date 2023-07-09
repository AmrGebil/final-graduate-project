from django.urls import path
from . import views


urlpatterns = [
    path('fristaid/', views.first_aidView, name="fristAid"),
    path('diseaseknowledge/', views.disease_knowledgeView, name="diseaseKnowledge"),

]