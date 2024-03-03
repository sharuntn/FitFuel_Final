from django.shortcuts import render
from django.contrib.auth.models import User, auth
from userprofile.models import UserProfile
from django.http import HttpResponseRedirect
from django.urls import reverse
from foodlens.models import Intake
from datetime import date
from django.shortcuts import render
from maintenance import calculate_bmr
from maintenance import calculate_maintenance_calories

L = []
# from foodlens.views import TOTAL_NUTRIENTS_TODAY

# back_to_label = {
#      'Normal Weight and Healthy':2500,
#      'Overweight':1500,
#      'Obesity Class 1':1200,
#      'Obesity Class 3':800,
#      'Obesity Class 2':1000,
#      'Slender':3000

# }

dietDict = {
    'd1': 'Balanced Diet',
    'd2': 'Mediterranean Diet',
    'd3': 'Keto Diet',
    'd4': 'Intermittent Fasting',
    'd5': 'Paleo Diet',
    'd6': 'DASH Diet',
    'd7': 'Zone Diet'
}

reverseDietDiet = {v:k for k,v in dietDict.items()}

categoryDict = {
    'c1': 'Slender',
    'c2': 'Normal Weight and Healthy',
    'c3': 'Overweight',
    'c4': 'Obesity Class 1',
    'c5': 'Obesity Class 2',
    'c6': 'Obesity Class 3'
}

reversecatogoryDict = {v:k for k,v in categoryDict.items()}

diabeticDict = {
    0: 'not_diabetic',
    1: 'diabetic',
    2: 'not_sure'
}

reverseDiabeticDict = {v:k for k,v in diabeticDict.items()}

def dietRec(category, diabetic):
    if diabetic == 'not_diabetic':
        if category == categoryDict['c1']:
            return dietDict['d1']
        elif category == categoryDict['c2']:
            return dietDict['d1']
        elif category == categoryDict['c3']:
            return dietDict['d6']
        elif category == categoryDict['c4']:
            return dietDict['d1']
        elif category == categoryDict['c5']:
            return dietDict['d1']
        elif category == categoryDict['c6']:
            return dietDict['d1']
    elif diabetic == 'diabetic':
        if category == categoryDict['c1']:
            return dietDict['d2']
        elif category == categoryDict['c2']:
            return dietDict['d2']
        elif category == categoryDict['c3']:
            return dietDict['d6']
        elif category == categoryDict['c4']:
            return dietDict['d3']
        elif category == categoryDict['c5']:
            return dietDict['d3']
        elif category == categoryDict['c6']:
            return dietDict['d3']
    elif diabetic == 'not_sure':
        if category == categoryDict['c1']:
            return dietDict['d7']
        elif category == categoryDict['c2']:
            return dietDict['d7']
        elif category == categoryDict['c3']:
            return dietDict['d7']
        elif category == categoryDict['c4']:
            return dietDict['d7']
        elif category == categoryDict['c5']:
            return dietDict['d7']
        elif category == categoryDict['c6']:
            return dietDict['d7']
        

def dashboardFunction(request):
    if request.user.is_authenticated:
        try:
            current_date = date.today()
            user_profile = UserProfile.objects.get(user=request.user)
            user_id = request.user.id
            bmr = calculate_bmr(user_profile.gender,user_profile.weight,user_profile.height,user_profile.age)
            total_calories = calculate_maintenance_calories(bmr,user_profile.activity_level)
            results = Intake.objects.filter(user=user_id,timestamp__date=current_date).values('calories')
            calorielist = []
            for i in results:
                calorielist.append(i['calories'])
            # print(sum(calorielist))
            calorie_left = total_calories - sum(calorielist)

            condition_key = reversecatogoryDict[user_profile.output]
            diet = categoryDict[condition_key]
            # print(diet)
            diabetic_key = reverseDiabeticDict[user_profile.diabetic]
            diabetic = diabeticDict[diabetic_key]
            # print(diabetic)

            recommended_diet = dietRec(diet,diabetic)

    

            return render(request, 'dashboard.html', {'user_profile': user_profile,'calorie_left': calorie_left,'total_calories':total_calories,'recommended_diet':recommended_diet})
        except UserProfile.DoesNotExist:
            # Handle the case where UserProfile doesn't exist for the user
            # Redirect to a page where user can set up their profile
            return HttpResponseRedirect(reverse('editprofile')) 
    else:
        # Redirect unauthenticated users to the login page
        return HttpResponseRedirect(reverse('login'))
    