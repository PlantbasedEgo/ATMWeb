from django.urls import path
from . views import UserRegisterView, UserLogInView, UserLogOutView

app_name = 'user_url'

urlpatterns = [
    path('signup/', UserRegisterView.as_view(), name= "user-register"),
    path('login/', UserLogInView.as_view(), name= "user-login"),
    path('logout/', UserLogOutView.as_view(), name= "user-logout"),

]
