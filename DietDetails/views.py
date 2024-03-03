from django.shortcuts import render
from userprofile.models import UserProfile

# Create your views here.
def Balance(request):
    return render(request,'BalenceDiet.html')

def Dash(request):
    return render(request,'Dash.html')

def Inter(request):
   
   return render(request,'Inter.html')

def Keto(request):
    return render(request,'Keto.html')

def Med(request):
   return render(request,'Med.html')

def Paleo(request):
    return render(request,'Paleo.html')

def Zone(request):
    return render(request,'Zone.html')

def Recommend(request):
    user_profile = UserProfile.objects.get(user=request.user)
    user_id = request.user.id
    return render(request,'Recommend.html',{'user_profile': user_profile})
