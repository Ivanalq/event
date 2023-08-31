from django.shortcuts import render, redirect




def index(request):
    return render(request, 'registr_user/register-user.html')






