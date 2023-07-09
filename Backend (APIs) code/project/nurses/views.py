from django.shortcuts import render
from .serializer import NurseSerializer,CitySerializer,SpecialtySerializer
from rest_framework import viewsets,permissions
from .models import Nurse,City,Specialty
from .filters import DoctorFilter
from rest_framework.pagination import PageNumberPagination



class NurseViewSet(viewsets.ModelViewSet):
    """
    http://localhost:8000/doctors/?his_specialty=1&his_city=1&search=tamer
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer
    filterset_class = DoctorFilter
    search_fields = ("his_name", "his_city__name", "his_specialty__name")
    pagination_class = PageNumberPagination
    http_method_names = ["get","head", "option"]

class CityViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = City.objects.all()
    serializer_class = CitySerializer
    http_method_names = ["get",  "head", "option"]


class SpecialtyViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
    http_method_names = ["get", "head", "option"]