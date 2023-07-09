from rest_framework import serializers
from .models import first_aid,disease_knowledge
class first_aidSerializers(serializers.ModelSerializer):

    class Meta:
        model = first_aid
        fields = '__all__'

class disease_knowledgeserializers(serializers.ModelSerializer):

    class Meta:
        model = disease_knowledge
        fields = '__all__'
