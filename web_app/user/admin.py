from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    #add_form = UserCreationForm
    #form = UserChangeForm
    model = User
    list_display = ["username", "email", "isBanned", "isOrganization", "inCheck", "phone_number", "birth_date", "name_organization"]

    

    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    
                    "email",
                    "isBanned",
                    "isOrganization",
                    "inCheck",
                    "phone_number",
                    "birth_date",
                    "name_organization",
                )
            }
        )
    )
    print(UserAdmin.fieldsets)
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    
                    
                    'isBanned',
                    'isOrganization',
                    'inCheck',
                    'phone_number',
                    'birth_date',
                    'name_organization',
                )
            } 
        )
    )

   


