from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.Home, name="home"),
    path('about-us', views.AboutUs, name="about-us"),
    path('contact', views.ContactUs, name="contact"),
    path('services', views.Services, name="services"),
    path('team', views.Team, name="team"),
    path('faqs', views.FAQs, name="faqs"),
]