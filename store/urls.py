from django.contrib import admin
from django.urls import path,include
from store import views

urlpatterns = [
    path('', views.home,name='home'),
    path('about', views.about,name='about'),
    path('contact', views.contact,name='contact'),
    path('order', views.order,name='order'),
    ]
