from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.foodlensFunction,name='FoodLens'),
    path('imageresult',views.foodlensresultFunction,name='foodLensResult'),
    path('add_to_intake/', views.add_to_intake, name='add_to_intake'),
    path('success/', views.success, name='success'),
    path('save_to_intake/', views.save_to_intake, name='save_to_intake'),
]
