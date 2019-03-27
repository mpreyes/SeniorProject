from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import caches
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.
from seniorProjectApp.models import *

def index(request):
    return render(request, 'seniorProjectApp/index.html')


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'seniorProjectApp/signup.html'


# def signup(request):
#     return render(request,'seniorProjectApp/signup.html')
#     #Signup MUST request a degree: Computer Science = 1


def dashboard(request, degreeID_id):
    #ERIN: add any field you want passed to the dashboard.html page
    user_details = []
    
    #getting courses from computer science only

    #if changing degree, change degreeID for both
    degree = Degree.objects.get(degreeID = degreeID_id)
    courses = Courses.objects.filter(degreeID = degreeID_id)

    #MR: set cache to pass in whatever level we want to show
    #MR TODO: Create a class to represent our entire class/link relationship
    #caches['levels'].set('level_freshman', level_freshman) 
    context = {"user_details": user_details,"degree_list": degree, "courses_list": courses}

    return render(request,'seniorProjectApp/dashboard.html',context)

def links(request,degreeID_id,courseID):

    courses = Courses.objects.filter(degreeID = degreeID_id)
    topics = Topics.objects.filter(courseID = courseID)
    #progress = 

    links = Links.objects.all()
   
    context = {"courses":courses, "topics": topics, "links": links, "checked_bool": True }
    return render(request,'seniorProjectApp/links.html',context)

