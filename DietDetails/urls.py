from django.urls import path
from . import views

urlpatterns = [
    path('bal/',views.Balance,),
    path('dash/',views.Dash),
    path('inter/',views.Inter,),
    path('keto/',views.Keto),
    path('med/',views.Med),
    path('paleo/',views.Paleo),
    path('zone/',views.Zone),
    path('',views.Recommend)
]