from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
import logging
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# @login_required(login_url='login')
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

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('home')

    return render (request,'login.html')
# def LoginPage(request):
#     logger = logging.getLogger(__name__)

#     if request.method == 'POST':
#         username = request.POST.get('username')
#         pass1 = request.POST.get('pass')

#         logger.debug(f"Attempting login for username: {username}")

#         user = authenticate(request, username=username, password=pass1)

#         if user is not None:
#             return HttpResponse("Username or Password is incorrect!!!")

#         else:
#             # logger.debug(f"Login failed for user: {username}")
#             # return HttpResponse("Username or Password is incorrect!!!")
#             login(request, user)
#             return redirect('home')



    return render(request, 'login.html')

    

def LogoutPage(request):
    logout(request)
    return redirect('login')

# def dsa_view(request):
#     return render(request, 'dsa.html')

# def csa_view(request):
#     return render(request, 'csa.html')

# def oop_view(request):
#     return render(request, 'oop.html')

# def fne_view(request):
#     return render(request, 'fne.html')

# def math_view(request):
#     return render(request, 'math.html')

def math_view(request):
    return render(request, 'subjects_1/math.html')

def fne_view(request):
    return render(request, 'subjects_1/fne.html')

def oop_view(request):
    return render(request, 'subjects_1/oop.html')

def csa_view(request):
    return render(request, 'subjects_1/csa.html')

def dsa_view(request):
    return render(request, 'subjects_1/dsa.html')
