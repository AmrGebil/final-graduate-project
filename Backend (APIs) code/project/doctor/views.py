from django.shortcuts import render
from .serializer import DoctorSerializer,CitySerializer,SpecialtySerializer
from rest_framework import viewsets ,permissions
from .models import Doctor,City,Specialty
from .filters import DoctorFilter
from rest_framework.pagination import PageNumberPagination

class DoctorViewSet(viewsets.ModelViewSet):

    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = DoctorFilter
    search_fields = ("his_name", "his_city__name","his_specialty__name")
    pagination_class = PageNumberPagination
    http_method_names = ["get","head", "option"]

class CityViewSet(viewsets.ModelViewSet):

    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get",  "head", "option"]


class SpecialtyViewSet(viewsets.ModelViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get", "head", "option"]