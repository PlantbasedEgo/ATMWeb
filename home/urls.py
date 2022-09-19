from django.urls import path

from . views import HomePageView

app_name = 'home_url'

urlpatterns = [
    path('', HomePageView.as_view(), name= "home-home"),
]
