from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from user.models import CustomUser
from . forms import DepositForm, TransferForm, WithdrawForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from datetime import datetime
from decimal import *
import json

log_count = 5
current_time = timezone.now()

# json.dumps() method but the method doesn't handle Decimal values by default.
# To solve the error, extend from the JSONEncoder class and convert Decimal values to a string when serializing them.
class Extra_JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        if isinstance(obj, datetime):
            return str(obj)
        return json.JSONEncoder.default(self, obj) # how about use super(). like in https://stackoverflow.com/questions/65338261/combine-multiple-json-encoders ?
        
class HomePageView(TemplateView):
    template_name = 'home/mainpage.html'  #default directory if template_name is not stated -> <app>/<model>_<viewtype>.html

class TransactionLogPageView(TemplateView):
    template_name = 'home/transactionlog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['user'] = CustomUser.objects.get(username = self.request.user)
        
        return context

class DepositPageView(LoginRequiredMixin, FormView):
    model = CustomUser
    template_name = 'home/deposit.html'
    form_class = DepositForm
    success_url = reverse_lazy('home_url:home-home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['current_user'] = CustomUser.objects.get(username = self.request.user.username)

        return context

    def form_valid(self, form):
        deposit_amount = form.cleaned_data['amount'] 
        current_user = CustomUser.objects.get(username = self.request.user.username)

        json_action_log = json.dumps({
            'username' : current_user.username,
            'first' : current_user.first_name, 
            # 'id' : current_user.id, TO BE IMPLEMENTED
            'type' : 'Deposit',
            'detail' : 'Deposit',
            'amount' : deposit_amount,
            'time' : current_time}, cls = Extra_JsonEncoder)    #cls specify which JsonEncoder to use when calling dumps(), in this case we use Extra_JsonEncoder

        if len(current_user.activities_log) > log_count:
            del current_user.activities_log[0]
     
        current_user.balance += deposit_amount
        current_user.activities_log.append(json_action_log)

        current_user.save()
        
        return super().form_valid(form)

class WithdrawPageView(LoginRequiredMixin, FormView):
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
        current_user = CustomUser.objects.get(username = self.request.user.username)
        json_action_log = json.dumps({
            'username' : current_user.username,
            'first' : current_user.first_name, 
            # 'id' : current_user.id, TO BE IMPLEMENTED
            'type' : 'Withdraw',
            'detail' : 'Withdraw',
            'amount' : withdraw_amount,
            'time' : current_time}, cls = Extra_JsonEncoder)  



        current_user.balance -= withdraw_amount
        current_user.activities_log.append(json_action_log)
        if len(current_user.activities_log) > log_count:
            del current_user.activities_log[0]

        current_user.save()

        return super().form_valid(form)

    def get_form_kwargs(self):  
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class TransferPageView(LoginRequiredMixin, FormView):
    model = CustomUser
    template_name = 'home/transfer.html'
    form_class = TransferForm
    success_url = reverse_lazy('home_url:home-home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # retrieve request user from query for writing logic in form_valid
        context['user'] = CustomUser.objects.get(username = self.request.user.username)

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
        current_user = CustomUser.objects.get(username = self.request.user.username)

        # Serialize obj
        json_action_log = json.dumps({
            'username' : current_user.username,
            'first' : current_user.first_name, 
            # 'id' : current_user.id, TO BE IMPLEMENTED
            'type' : 'Transfer',
            'recipient' : receive_user.username,
            'amount' : withdraw_amount,
            'time' : current_time}, cls = Extra_JsonEncoder)  

        json_recipient_log = json.dumps({
            'username' : receive_user.username,
            'first' : receive_user.first_name, 
            # 'id' : current_user.id, TO BE IMPLEMENTED
            'type' : 'Transfer',
            'donor' : receive_user.username,
            'amount' : withdraw_amount,
            'time' : current_time}, cls = Extra_JsonEncoder)  

        # append and delete transaction log in activities_log 
        current_user.activities_log.append(json_action_log)
        receive_user.activities_log.append(json_recipient_log)
        if len(current_user.activities_log)> log_count:
            del current_user.activities_log[0]
        if len(receive_user.activities_log)> log_count:
            del receive_user.activities_log[0]

        current_user.balance -= withdraw_amount
        receive_user.balance += withdraw_amount

        # save data of request user
        current_user.save()
        receive_user.save()
        
        return super().form_valid(form)

    def get_form_kwargs(self):  #Sending user to the form.py, since basic form and ModelForm can't 
        kwargs = super().get_form_kwargs()

        kwargs.update({'user': self.request.user})

        return kwargs

