from .serializer import first_aidSerializers,disease_knowledgeserializers
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets, permissions
from .models import first_aid , disease_knowledge

# Create your views here.
class first_aid_view(viewsets.ModelViewSet):
    queryset = first_aid.objects.all()
    serializer_class = first_aidSerializers
    search_fields = ("name", "desciption")
    pagination_class = PageNumberPagination
    http_method_names = ["get", "head", "option"]

class disease_knowledge_view(viewsets.ModelViewSet):
    queryset = disease_knowledge.objects.all()
    serializer_class = disease_knowledgeserializers
    search_fields = ("name", "desciption")
    pagination_class = PageNumberPagination
    http_method_names = ["get", "head", "option"    ]
