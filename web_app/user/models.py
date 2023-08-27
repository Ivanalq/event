from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    isBanned = models.BooleanField(default=False)
    isOrganization = models.BooleanField(default=False)
    inCheck = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=100, blank=True, default='+79533484285')
    birth_date = models.DateField(null=True, blank=True)
    name_organization = models.CharField(max_length=200, blank=True)
