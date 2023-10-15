"""registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    # path('dsa/', views.dsa_view, name='dsa'),
    # path('csa/', views.csa_view, name='csa'),
    # path('oop/', views.oop_view, name='oop'),
    # path('fne/', views.fne_view, name='fne'),
    # path('math/', views.math_view, name='math'),
    path('subjects_1/math/', views.math_view, name='math'),
    path('subjects_1/fne/', views.fne_view, name='fne'),
    path('subjects_1/oop/', views.oop_view, name='oop'),
    path('subjects_1/csa/', views.csa_view, name='csa'),
    path('subjects_1/dsa/', views.dsa_view, name='dsa'),



    
]