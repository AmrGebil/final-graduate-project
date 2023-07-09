from django.urls import path
from .views import home,RegisterView,profile,contact_us,service,about_us,medicalhistory

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('contactus/', contact_us, name='contact_us'),
    path('services/', service, name='services'),
    path('aboutus/', about_us, name='about_us'),
    path('medicalhistory/', medicalhistory, name='medicalhistory'),

]