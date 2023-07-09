from rest_framework import serializers
from .models import Nurse, City, Specialty, Governorate

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name']

class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = ['name']

class GovernorateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Governorate
        fields = ['name']

class NurseSerializer(serializers.ModelSerializer):
    his_city = CitySerializer()
    his_specialty = SpecialtySerializer()
    his_governorate = GovernorateSerializer()

    class Meta:
        model = Nurse
        fields = '__all__'