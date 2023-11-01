from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
import logging
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')
    

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    
    return render (request,'signup.html')

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def LoginPage(request):
    error_message = None  

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Invalid username or password. Please try again."

    return render(request, 'login.html', {'error_message': error_message})


from django.shortcuts import render
from django.contrib import messages

def LogoutPage(request):
    logout(request)
    messages.success(request, "Successful Logout")
    return render(request, 'logout.html', {'success_message': messages.get_messages(request)})

def computer_system_architecture(request):
    return render(request, 'subjects_1/computer_system_architecture.html')

def introduction_to_data_analytics(request):
    return render(request, 'subjects_1/introduction_to_data_analytics.html')

def data_structures(request):
    return render(request, 'subjects_1/data_structures.html')

def mathematical_foundations(request):
    return render(request, 'subjects_1/mathematical_foundations.html')

def object_oriented_programming(request):
    return render(request, 'subjects_1/object_oriented_programming.html')

def finance_econometrics(request):
    return render(request, 'subjects_1/finance_econometrics.html')

def profile(request):
    if request.method=='POST':
        user = User.objects.get(user=request.user)
        user.username=user.username
    return render(request, 'profile.html')

from django import forms
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})
