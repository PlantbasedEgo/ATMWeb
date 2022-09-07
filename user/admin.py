from django.contrib import admin
from . models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea

class UserAdminConfig(UserAdmin):

    model = CustomUser

    list_display = ('email','user_id','username','first_name','last_name','is_active',
     'is_staff', 'is_superuser') #Set list_display to control which fields are displayed on the change list page
    ordering = ('-is_staff', '-username') #Set ordering to specify how lists of objects should be ordered in the Django admin views
    search_fields = ('email','user_id','username','first_name','last_name') #Set search_fields to enable a search box on the admin change list page
    list_filter = ('username','first_name','last_name','is_active','is_staff','is_superuser') #Set list_filter to activate filters in the right sidebar of the change list page of the admin.

    add_fieldsets = (
        (None,      {'classes': ['wide'], 
                     'fields': ['email','username','first_name','last_name','password1','password2']}
        ), 
    ) #add_fieldsets (for fields to be used when creating a user)

    fieldsets = (
        (None,          {'fields': ('email', 'username', 'first_name', 'last_name')}),
        ('Permission',  {'fields': ('is_staff', 'is_active')}),
        ('Personal',    {'fields': ['about']}),
    ) #fieldsets (for fields to be used in editing users)

    
    formfield_overrides = {
        CustomUser.about: {'widget' : Textarea(attrs={'rows':10, 'cols':40})},
        
    } #a quick-and-dirty way to override some of the Field options for use in the admin.


        
admin.site.register(CustomUser, UserAdminConfig)
