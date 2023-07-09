from django.urls import path
from . import views

# 'jobs/' the main link
urlpatterns = [
    path('', views.nurses, name="nurses_List"),
    path('<int:id>', views.nurse_detailes, name="nurse_detailes"),

]