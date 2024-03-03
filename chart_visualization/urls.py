from django.contrib import admin
from django.urls import path, include


from . import views

urlpatterns = [
    path('',views.chart_pg,name='chart_home')
]

