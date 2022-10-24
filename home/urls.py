from django.urls import path

from . views import HomePageView, DepositPageView, WithdrawPageView, TransferPageView, TransactionLogPageView

app_name = 'home_url'

urlpatterns = [
    path('', HomePageView.as_view(), name= "home-home"),
    path('transactionlog/', TransactionLogPageView.as_view(), name= "home-transactionlog"),
    path('deposit/', DepositPageView.as_view(), name= "home-deposit"),
    path('withdraw/', WithdrawPageView.as_view(), name= "home-withdraw"),
    path('transfer/', TransferPageView.as_view(), name= "home-transfer"),
    
]
