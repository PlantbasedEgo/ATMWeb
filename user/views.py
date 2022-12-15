from django.shortcuts import render
from django.views.generic import CreateView
from . forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin

class UserRegisterView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home_url:home-home') #use reverse_lazy to use URL name, instead of URL path
    template_name = "user/signup.html" #default directory if template_name is not stated -> <app>/<model>_<viewtype>.html
    success_message = "User has been registered successfully"
    
class UserLogInView(LoginView):
    template_name = "user/login.html"

class UserLogOutView(LogoutView):
    # template_name can be dropped if there is next_page, because next_page will overwrite template_name
    next_page = reverse_lazy("home_url:home-home")      
