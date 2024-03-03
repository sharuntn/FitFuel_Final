from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

def loginFunction(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    return render(request,'login.html')

def registerFunction(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if len(password1) < 8:
            messages.error(request, "The password must be at least 8 characters long.")
            return render(request, 'base/register.html')

        if password1.lower().startswith(username.lower()) or \
                password1.lower().startswith(first_name.lower()) or \
                password1.lower().startswith(last_name.lower()):
            messages.error(request, "The password is too similar to the username, first name, or last name.")
            return render(request, 'register.html')

        if not any(char.isupper() for char in password1):
            messages.error(request, "The password must contain at least one capital letter.")
            return render(request, 'register.html')
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Taken")
                return redirect('register')
            else:
                user =User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print("user created")
                return redirect('dashboard')
        else:
            messages.info(request,"Password not matching")
            return redirect('Register')
        return redirect('dashboard')  # Redirect to the home page after registration

    else:
        return render(request,'register.html')
    

def lgout(request):
    auth.logout(request)
    return redirect('login')
