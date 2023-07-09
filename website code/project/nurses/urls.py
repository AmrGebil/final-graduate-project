from django.urls import path
from . import views


urlpatterns = [
    path('', views.nurses, name="nurses_List"),
    path('<int:id>', views.nurse_detailes, name="nurse_detailes"),

]