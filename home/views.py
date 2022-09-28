from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from user.models import CustomUser
from . forms import DepositForm
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'home/mainpage.html'  #default directory if template_name is not stated -> <app>/<model>_<viewtype>.html

class DepositPageView(FormView):
    model = CustomUser
    template_name = 'home/deposit.html'
    form_class = DepositForm
    success_url = reverse_lazy('home_url:home-home')

    def form_valid(self, form):
        deposit_amount = form.cleaned_data['amount']
        self.request.user.balance += deposit_amount
        self.request.user.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = CustomUser.objects.get(username = self.request.user)
        return context
 
class WithdrawPageView(FormView):
    pass

class TransferPageView(FormView):
    pass