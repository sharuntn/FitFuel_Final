from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.core.exceptions import ObjectDoesNotExist
from recommentation import predict_diet
# Create your views here.
def userprofileFunction(request):
    user_profile = UserProfile.objects.get(user=request.user)
    user_id = request.user.id
    return render(request,'userprofile.html',{'user_profile' : user_profile,'user_id': user_id})

@login_required
def editprofileFunction(request): 
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except ObjectDoesNotExist:
        user_profile = UserProfile(user=request.user)

    if request.method == 'POST':
        user_profile.age = request.POST.get('age')
        user_profile.dob = request.POST.get('dob')
        user_profile.mobile = request.POST.get('mobile')
        user_profile.weight = request.POST.get('weight')
        user_profile.height = request.POST.get('height')
        user_profile.abdomen = request.POST.get('abdomen')
        user_profile.diabetic = request.POST.get('diabetic', 'not_sure')
        user_profile.gender = request.POST.get('gender','Male')
        user_profile.activity_level = request.POST.get('activity_level',1.85)
        user_profile.profile_picture = request.FILES.get('profile_picture')

        #BMI
        weight_kg = float(user_profile.weight)
        height_m = float(user_profile.height) / 100  # Convert height to meters
        abdomen_m = float(user_profile.abdomen)/100  #Convert abdomen to meters
        user_age = user_profile.age
        user_profile.bmi = round(weight_kg / (height_m ** 2), 2)
        user_profile.output = predict_diet(user_age,weight_kg,height_m,abdomen_m)
        
        user_profile.save()
        
        return redirect('userprofile')
    return render(request,'editprofile.html',{'user_profile': user_profile})