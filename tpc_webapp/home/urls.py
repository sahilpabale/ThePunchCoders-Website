from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='HomePage'),
    path('about', views.about, name='AboutPage'),
    path('contact', views.contact, name='ContactUsPage'),
    path('search', views.search, name='SearchPage'),
]