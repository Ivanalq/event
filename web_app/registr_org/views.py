from django.shortcuts import render

def index(request):
    return render(request, 'registr_org/registration-org.html')
