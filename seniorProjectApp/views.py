from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import caches

# Create your views here.
from seniorProjectApp.models import *

def index(request):
    return render(request, 'seniorProjectApp/index.html')


def signup(request):
    return render(request,'seniorProjectApp/signup.html')
    #Signup MUST request a degree: Computer Science = 1

def dashboard(request):
    #ERIN: add any field you want passed to the dashboard.html page

    #getting courses from computer science only
    degree = Degree.objects.get(degreeID = 1)
    courses = Courses.objects.filter(degreeID = 1)

    #MR: set cache to pass in whatever level we want to show
    #MR TODO: Create a class to represent our entire class/link relationship
    #caches['levels'].set('level_freshman', level_freshman) 
    context = {"degree_list": degree, "courses_list": courses}

    return render(request,'seniorProjectApp/dashboard.html',context)

def links(request):
   
    #context = {"levels":  caches['levels'].get('level_freshman')}
    class_1_links = [ "link1", "link","link2","link2","link3","link3","link4","linky"]
    context = {"links": class_1_links}
    return render(request,'seniorProjectApp/links.html',context)

