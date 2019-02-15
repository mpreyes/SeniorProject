from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'seniorProjectApp/index.html')


def signup(request):
    return render(request,'seniorProjectApp/signup.html')

def dashboard(request):
    return render(request,'seniorProjectApp/dashboard.html')

def links(request):
    return render(request,'seniorProjectApp/links.html')

