from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from accounts.views import signup, login, logout


app_name = 'accounts'

urlpatterns =[
    path('signup/',views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home'),
    path('main/', views.main, name="main"),
    path('main1/', views.main1, name="main1"),
    path('home/popup/',views.popup, name='popup'),
]