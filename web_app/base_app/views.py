from django.shortcuts import render
from django.shortcuts import HttpResponse



def index(request):
    
    print(3)
    
    return render(request, 'base_app/home-page.html')



