from django.urls import path
from . import views

urlpatterns = [
  path('', views.blogpost, name='blog'),
  path('<str:slug>', views.blogdetails, name='blogdetails'),
]