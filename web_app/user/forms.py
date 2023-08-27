from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "isBanned", "isOrganization", "inCheck", "phone_number", "birth_date", "name_organization")

class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "email", "isBanned", "isOrganization", "inCheck", "phone_number", "birth_date", "name_organization")