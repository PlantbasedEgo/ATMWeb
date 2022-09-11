from django.urls import path
from . views import UserSignUpView

app_name = 'user_url'

urlpatterns = [
    path('signup/', UserSignUpView.as_view(), name= "user-signup")

]
