from django.urls import path,include
from rest_framework import routers
from .views import DoctorViewSet ,CityViewSet,SpecialtyViewSet

router = routers.DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'cities', CityViewSet)
router.register(r'specialty', SpecialtyViewSet)
urlpatterns = [
    path('', include(router.urls)),
]











