from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from accounts.views import signup, login, logout


app_name = 'setting'

urlpatterns =[
    path('inbody/', views.inbody, name='inbody'),
    path('inbody_update/',views.inbody_update, name='inbody_update'),
    path('inbody_detail/',views.inbody_detail, name="inbody_detail")


]