from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.mail import send_mail


def index(request):
    
    
    
    return render(request, 'base_app/home-page.html')



