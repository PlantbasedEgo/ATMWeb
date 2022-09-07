from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from . manager import CustomAccountManager



# --------------------Customize User---------------------------

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_("Username"), max_length=15, unique=True)
    first_name = models.CharField(_("First Name"), max_length=15)
    last_name = models.CharField(_("Last Name"), max_length=25)
    email = models.EmailField(_("Email Address"), unique=True)
    balance = models.DecimalField(max_digits=12, decimal_places=3, default=0, null=True)
    withdrawal_fee = models.DecimalField(max_digits=6, decimal_places=4, default=1.0005, null=True)
    user_id = models.DecimalField(max_digits=5, decimal_places=0, default=0, null=True)
    #---------------------------------------------
    about = models.TextField(_("About"), max_length=250, blank=True)
    date_joined = models.DateTimeField(_("Date join"), default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'        #A string describing the name of the field on the user model that is used as the unique identifier. DEFAULT : USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']   #A list of the field names that will be prompted for when creating a user via the createsuperuser. DEFAULT : REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username
