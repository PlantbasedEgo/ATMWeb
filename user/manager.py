from django.contrib.auth.models import BaseUserManager



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
        extra_fields.setdefault("balance", None)            #set balance to Null for superuser 
        extra_fields.setdefault("withdrawal_fee", None)     #set withdrawal_fee to Null for superuser
        extra_fields.setdefault("user_id", None)            #set user_id to Null for superuser
        

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        
        return self._create_user(username, email, first_name, last_name, password, **extra_fields)
