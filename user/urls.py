from django.urls import path
from . views import UserSignUpView, UserLogInView, UserLogOutView

app_name = 'user_url'

urlpatterns = [
    path('signup/', UserSignUpView.as_view(), name= "user-signup"),
    path('login/', UserLogInView.as_view(), name= "user-login"),
    path('logout/', UserLogOutView.as_view(), name= "user-logout"),

]
