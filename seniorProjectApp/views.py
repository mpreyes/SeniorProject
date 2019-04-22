from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.cache import caches

from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm, ProgressForm

# Create your views here.
from seniorProjectApp.models import *

def index(request):
    return render(request, 'seniorProjectApp/index.html')


# def signup(request):
#     return render(request,'seniorProjectApp/signup.html')
#     #Signup MUST request a degree: Computer Science = 1


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'seniorProjectApp/signup.html'



def dashboard(request,id, degreeID_id):
    #ERIN: add any field you want passed to the dashboard.html page
    user_details = []
    
    #getting courses from computer science only

    #if changing degree, change degreeID for both
    user = CustomUser.objects.get(id = id)
    degree = Degree.objects.get(degreeID = degreeID_id)
    courses = Courses.objects.filter(degreeID = degreeID_id)

    #MR: set cache to pass in whatever level we want to show
    #MR TODO: Create a class to represent our entire class/link relationship
    #caches['levels'].set('level_freshman', level_freshman) 
    context = {"user_details": user_details,"degree_list": degree, "courses_list": courses}

    return render(request,'seniorProjectApp/dashboard.html',context)

def links(request,degreeID_id,courseID):
    
    
    courses = Courses.objects.get(courseID = courseID)
    topics = Topics.objects.filter(courseID = courseID)
    links = Links.objects.all()
    progress = Progress.objects.all()
    link_progress = zip(links,progress)
    context = {"course": courses, "topics": topics, "links": links, "link_progress": link_progress} 

    if request.method == 'POST':
        print("got a post request")
        form = ProgressForm(request.POST)
        
        if form.is_valid():
            form.save()
            print("form got saved")
            context["form"] = form
            
            return render(request,'seniorProjectApp/links.html',context)
    else:
        print("Form did not get saved")
        form = ProgressForm()
    context["form"] = form
        
        
    
    return render(request,'seniorProjectApp/links.html',context)

