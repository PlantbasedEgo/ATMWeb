from django.shortcuts import render
from django.views.generic import CreateView
from . forms import CustomUserCreationForm
from django.urls import reverse_lazy

class UserSignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home_url:home-home')
    template_name = "user/Register.html" #default directory if template_name is not stated -> <app>/<model>_<viewtype>.html
    
 
    