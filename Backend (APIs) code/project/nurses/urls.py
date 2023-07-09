from django.urls import path,include
from rest_framework import routers
from .views import NurseViewSet,SpecialtyViewSet,CityViewSet
router = routers.DefaultRouter()
router.register(r'nursesfilter', NurseViewSet)
router.register(r'cities', CityViewSet)
router.register(r'specialty', SpecialtyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]