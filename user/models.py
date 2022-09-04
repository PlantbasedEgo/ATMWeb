from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager): #Create Manager for CustomUser

    #-------------------------Base-------------------------------
    def _create_user(self, username, email, first_name, last_name, password, **extra_fields):

        if not email:
            raise ValueError("The given username must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    #-----------------------Create Normal User----------------------
    def create_user(self, username, email, first_name, last_name, password, **extra_fields):

        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        return self._create_user(username, email, first_name, last_name, password, **extra_fields)
        
    #---------------------Create Super User------------------------------
    def create_superuser(self, username, email, first_name, last_name, password, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        
        return self._create_user(username, email, first_name, last_name, password, **extra_fields)


# --------------------Customize User---------------------------

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_("Username"), max_length=15, unique=True)
    first_name = models.CharField(_("First Name"), max_length=15)
    last_name = models.CharField(_("Last Name"), max_length=25)
    email = models.EmailField(_("Email Address"), unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=5, default=0)
    withdrawal_fee = models.DecimalField(max_digits=6, decimal_places=6, default=1.0005)
    user_id = models.DecimalField(max_digits=5, decimal_places=0, default=0)
    #---------------------------------------------
    about = models.TextField(_("About"), max_length=250, blank=True)
    date_joined = models.DateTimeField(_("Date join"), default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'        #A string describing the name of the field on the user model that is used as the unique identifier. DEFAULT : USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']   #A list of the field names that will be prompted for when creating a user via the createsuperuser. DEFAULT : REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.user_name
