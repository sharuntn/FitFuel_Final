from django.shortcuts import render,redirect
from .mingo import prediction
from .forms import ImageForm,IntakeForm
from userprofile.models import UserProfile
from .models import Nutrients,Intake
from django.http import JsonResponse

# Create your views here.



def foodlensFunction(request):
    user_profile = UserProfile.objects.get(user=request.user)
    form = ImageForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        img_obj = form.instance
            
        return render(request,'foodlens.html',{'form':form,'img_obj':img_obj})
    else:
        form = ImageForm()
        return render(request,'foodlens.html', {'form': form,'user_profile':user_profile})


def foodlensresultFunction(request):
    global TOTAL_NUTRIENTS_TODAY
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            predicted_food = prediction(img_obj.image.path)
            calories = get_calories_for_food(predicted_food)
            # print(TOTAL_NUTRIENTS_TODAY)
            return render(request, 'foodlensresult.html', {'predicted_food': predicted_food, 'calories': calories,'img_obj':img_obj,'user_profile': user_profile})
            print(calories)
    else:
        form = ImageForm()
    return render(request, 'foodlens.html', {'form': form})

def get_calories_for_food(food_name):
    nutrients = Nutrients.objects.filter(food=food_name).first()   
    if nutrients:
        return nutrients.energy  # Assuming 'energy' field represents calories
    return None

# def get_calories_for_food(request):
#     calories_data = Intake.objects.filter(user=request.user).values_list('timestamp', 'calories')
#     return JsonResponse(list(calories_data), safe=False)

def add_to_intake(request):
    print(request.user)  # Check the value of request.user
    if request.method == 'POST':
        form = IntakeForm(request.POST)
        if form.is_valid():
            intake = form.save(commit=False)
            intake.user = request.user  # Assign the current user to the 'user' field
            intake.save()
            return redirect('success')  # Redirect to a success page or another view
    else:
        form = IntakeForm()
    return render(request, 'add_to_intake.html', {'form': form})

def success(request):
    return render(request, 'success.html')

def save_to_intake(request):
    if request.method == 'POST':
        form = IntakeForm(request.POST)
        if form.is_valid():
            quantity = request.POST['quantity']  # Access quantity value from request.POST
            intake = form.save(commit=False)
            intake.user = request.user  # Assign the current user to the 'user' field
            intake.quantity = quantity  # Assign quantity value to the 'quantity' field
            if 'quantity' in form.cleaned_data:
                quantity = form.cleaned_data['quantity']
            else:
                quantity = 1  # Default quantity if not provided
            
            calories_per_unit = form.cleaned_data['calories']
            total_calories = quantity * calories_per_unit
            
            intake.calories = total_calories
            intake.save()
            return redirect('success')  # Redirect to a success page or another view
    else:
        form = IntakeForm()
    # If the request method is not POST or the form is not valid, render the form again
    return render(request, 'add_to_intake.html', {'form': form})
# def save_to_intake(request):
    if request.method == 'POST':
        form = IntakeForm(request.POST)
        if form.is_valid():
            intake = form.save(commit=False)
            intake.user = request.user  # Assign the current user to the 'user' field
            
            # Ensure 'quantity' field is present in the form's cleaned_data
            if 'quantity' in form.cleaned_data:
                quantity = form.cleaned_data['quantity']
            else:
                quantity = 1  # Default quantity if not provided
            
            calories_per_unit = form.cleaned_data['calories']
            total_calories = quantity * calories_per_unit
            
            intake.calories = total_calories
            intake.save()
            
            return redirect('success')
    else:
        form = IntakeForm()
    
    return render(request, 'add_to_intake.html', {'form': form})

