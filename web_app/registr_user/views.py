from django.shortcuts import render

def index(request):
    return render(request, 'registr_user/register-user.html')
