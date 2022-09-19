from django.shortcuts import render
from django.views.generic import CreateView
from . forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

class UserSignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home_url:home-home') #use reverse_lazy to use URL name, instead of URL path
    template_name = "user/register.html" #default directory if template_name is not stated -> <app>/<model>_<viewtype>.html
    
class UserLogInView(LoginView):
    template_name = "user/login.html"

class UserLogOutView(LogoutView):
    template_name = "user/logout.html"