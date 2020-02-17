from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('contact/', views.contact, name='contact'),
  path('about/', views.about, name='about'),
  path('search/', views.search, name='search'),
  path('singup/', views.getSingup, name='singup'),
  path('login/', views.getLogin, name='login'),
  path('logout/', views.getLogOut, name='logout'),
] 