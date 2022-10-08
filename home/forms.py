from django import forms
from user.models import CustomUser


class DepositForm(forms.Form):
    amount = forms.DecimalField(max_digits=12, decimal_places=3)

class WithdrawForm(forms.ModelForm):
    amount = forms.DecimalField(max_digits=12, decimal_places=3)
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['amount', 'confirm_password']

    def __init__(self, *args, **kwargs): # *connects with def get_context_data(self, **kwargs):
        self.user = kwargs.pop('user')

        super().__init__(*args, **kwargs)
    
    def clean(self):
        cleaned_data = super().clean()
        confirm_password = cleaned_data.get("confirm_password")

        #check if the password user type is correct before withdraw
        if not self.user.check_password(confirm_password):          
            raise forms.ValidationError("Please reenter your password")

class TransferForm(forms.ModelForm):
    amount = forms.DecimalField(max_digits=12, decimal_places=3)
    receive_username = forms.CharField(max_length=15)
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['amount', 'receive_username', 'confirm_password']
    
    def __init__(self, *args, **kwargs): # *connects with def get_context_data(self, **kwargs):
        self.user = kwargs.pop('user')
        
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        confirm_password = cleaned_data.get("confirm_password")

        #check if the password user type is correct before withdraw
        if not self.user.check_password(confirm_password):          
            raise forms.ValidationError("Please reenter your password")
        
        