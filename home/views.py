from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home/mainpage.html'  #default directory if template_name is not stated -> <app>/<model>_<viewtype>.html