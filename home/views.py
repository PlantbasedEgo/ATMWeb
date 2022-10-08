from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from user.models import CustomUser
from . forms import DepositForm, TransferForm, WithdrawForm
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'home/mainpage.html'  #default directory if template_name is not stated -> <app>/<model>_<viewtype>.html

class DepositPageView(FormView):
    model = CustomUser
    template_name = 'home/deposit.html'
    form_class = DepositForm
    success_url = reverse_lazy('home_url:home-home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['user'] = CustomUser.objects.get(username = self.request.user)

        return context

    def form_valid(self, form):
        deposit_amount = form.cleaned_data['amount'] 

        self.request.user.balance += deposit_amount

        self.request.user.save()
        
        return super().form_valid(form)

class WithdrawPageView(FormView):
    model = CustomUser
    template_name = 'home/withdraw.html'
    form_class = WithdrawForm
    success_url = reverse_lazy('home_url:home-home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['user'] = CustomUser.objects.get(username = self.request.user)

        return context

    def form_valid(self, form):
        withdraw_amount = form.cleaned_data['amount']

        self.request.user.balance -= withdraw_amount

        self.request.user.save()

        return super().form_valid(form)

    def get_form_kwargs(self):  
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class TransferPageView(FormView):
    model = CustomUser
    template_name = 'home/transfer.html'
    form_class = TransferForm
    success_url = reverse_lazy('home_url:home-home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # retrieve request user from query for writing logic in form_valid
        context['user'] = CustomUser.objects.get(username = self.request.user)
        return context

    def form_valid(self, form, **kwargs):
        # retrieve info from form after validation
        withdraw_amount = form.cleaned_data['amount'] 
        receive_username = form.cleaned_data['receive_username']
        
        # get the receive_username from cleaned_data and put it into context
        context = self.get_context_data(**kwargs)
        context['receive_username'] = CustomUser.objects.get(username = receive_username)

        # get receive_username from query
        receive_user = CustomUser.objects.get(username = receive_username)

        self.request.user.balance -= withdraw_amount
        receive_user.balance += withdraw_amount

        # save data of request user
        self.request.user.save()

        return super().form_valid(form)

    def get_form_kwargs(self):  #Sending user to the form.py, since basic form and ModelForm can't 
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs
