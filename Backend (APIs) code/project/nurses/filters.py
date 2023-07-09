import django_filters
from .models import Nurse

class DoctorFilter(django_filters.FilterSet):
    specialty_filter = django_filters.CharFilter(lookup_expr='icontains')
    cit_filter = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Nurse
        fields = ['his_city','his_specialty']
