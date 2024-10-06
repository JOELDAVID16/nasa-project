from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import RedirectView
from .views import signup

urlpatterns = [
    path('login/', views.auth_login, name='login'),
    path('register/', signup, name='register'),
    path('login/register', signup, name='register'),
    path('index', views.index,name="index"),
    path('', views.index,name="index"),
    path('home/', views.home,name='home'),
    path('advance/', views.advance,name='advance'),
    path('login/advance/', views.advance,name='advance'),
    path('intermediate/', views.intermediate,name='intermediate'),
    path('login/intermediate/', views.intermediate,name='intermediate'),
    path('beginner/',views.beginner,name='beginner'),
    path('login/beginner/',views.beginner,name='beginner'),
]