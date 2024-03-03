from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('login/',views.loginFunction,name='login'),
    path('register/',views.registerFunction,name='register'),
    path('logout/',views.lgout,name="logout"),
    
]