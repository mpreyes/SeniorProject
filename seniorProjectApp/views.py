from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import caches

# Create your views here.
from seniorProjectApp.models import *

def index(request):
    return render(request, 'seniorProjectApp/index.html')


def signup(request):
    return render(request,'seniorProjectApp/signup.html')

def dashboard(request):
    #ERIN: add any field you want passed to the dashboard.html page
    data = Courses.objects.all()

    level_freshman = [{"name": "intro to programming", "description": "intro  to programming teaches you the basics of programming, including..", "color":
     "blue", "links" : "1"},{"name": "class2", "description": "intro  to programming teaches you the basics of programming, including..", "color": "blue"},
     {"name": "class3", "description": "intro  to programming teaches you the basics of programming, including..","color": "blue", },{"name": "class4", 
      "description": "intro  to programming teaches you the basics of programming, including..", "color": "blue"}, {"name": "class5", "description": "intro  to programming teaches you the basics of programming, including..",
       "color": "blue"},{"name": "class6",  "description": "intro  to programming teaches you the basics of programming, including..",
       "color": "blue"}]

    #MR: set cache to pass in whatever level we want to show
    #MR TODO: Create a class to represent our entire class/link relationship
    #caches['levels'].set('level_freshman', level_freshman) 
    context = {"classes_list": data}
    #print("context " + str(context["classes_list"]))

    return render(request,'seniorProjectApp/dashboard.html',context)

def links(request):
   
    #context = {"levels":  caches['levels'].get('level_freshman')}
    class_1_links = [ "link1", "link","link2","link2","link3","link3","link4","linky"]
    context = {"links": class_1_links}
    return render(request,'seniorProjectApp/links.html',context)

