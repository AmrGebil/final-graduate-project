

from .views import RegisterAPI,LoginAPI
from django.urls import path, include
from knox import views as knox_views
from .views import UserProfileListCreateView, UserProfileRetrieveUpdateDeleteView,MedicalHistoryRetrieveUpdateDeleteView,MedicalHistoryListCreateView


urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

    path('profiles/', UserProfileListCreateView.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', UserProfileRetrieveUpdateDeleteView.as_view(), name='profile-retrieve-update-delete'),

    path('medicalmistory/', MedicalHistoryListCreateView.as_view(), name='medicalmistory-list-create'),
    path('medicalmistory/<int:pk>/', MedicalHistoryRetrieveUpdateDeleteView.as_view(), name='medicalmistory-retrieve-update-delete'),

]

