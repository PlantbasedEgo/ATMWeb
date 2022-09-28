from django import forms
from user.models import CustomUser


class DepositForm(forms.ModelForm):
    amount = forms.DecimalField(max_digits=12, decimal_places=3)

    class Meta:
        model = CustomUser
        fields = ['amount']

