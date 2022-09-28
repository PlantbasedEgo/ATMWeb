from django.urls import path

from . views import HomePageView, DepositPageView, WithdrawPageView, TransferPageView

app_name = 'home_url'

urlpatterns = [
    path('', HomePageView.as_view(), name= "home-home"),
    path('deposit/', DepositPageView.as_view(), name= "home-deposit"),
    path('withdraw/', WithdrawPageView.as_view(), name= "home-withdraw"),
    path('transfer/', TransferPageView.as_view(), name= "home-transfer"),
]
