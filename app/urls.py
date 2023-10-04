from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('services/', views.services, name='service'),
]
