from django.urls import path, include
from rest_framework import routers
from .views import first_aid_view, disease_knowledge_view

router = routers.DefaultRouter()
router.register('aid', first_aid_view)
router.register('disease', disease_knowledge_view)
urlpatterns = [
    path('', include(router.urls)),

]