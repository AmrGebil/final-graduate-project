import django_filters
from .models import Doctor

class DoctorFilter(django_filters.FilterSet):
    specialty_filter = django_filters.CharFilter(lookup_expr='icontains')
    cit_filter = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Doctor
        fields = ['his_city','his_specialty']
