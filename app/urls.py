from django.urls import path
from app import views

urlpatterns = [
    path('index',views.IndexVw, name="index"),
    path('About',views.AboutVw, name="about"),
    path('service',views.ServiceVw, name="service"),
    path('cars',views.CarsVw, name="cars"),
    path('Contact',views.ContactVw, name="contactus"),
    path('login',views.LoginVw, name="login"),
    path('registration',views.RegistrationVw, name="registration"),
]