from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse


def index(request):
    """Home page"""
    return render(request,'Gymobile_app/index.html')
