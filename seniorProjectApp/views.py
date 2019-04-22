from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.core.cache import caches
from django.shortcuts import render, get_object_or_404
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

def redirectme(request):
    degreeID  = 1
    userID = 1
    if request.user.is_authenticated:
        degreeID = request.user.degreeID
        userID = request.user.id

    return redirect("/seniorProjectApp/"  + str(userID) + "/" + str(degreeID)+ "/")


def dashboard(request,userID_id,degreeID):
    #ERIN: add any field you want passed to the dashboard.html page

    
    #getting courses from computer science only
    
    #if changing degree, change degreeID for both

    degree = Degree.objects.get(degreeID = degreeID)
    courses = Courses.objects.filter(degreeID = degreeID)

    #MR: set cache to pass in whatever level we want to show
    #MR TODO: Create a class to represent our entire class/link relationship
    #caches['levels'].set('level_freshman', level_freshman) 
    context = { "degree_list": degree, "courses_list": courses}

    return render(request,'seniorProjectApp/dashboard.html',context)
    

def links(request,userID_id,degreeID_id,courseID):
    #testUser = 1
    
    courses = Courses.objects.get(courseID = courseID)
    topics = Topics.objects.filter(courseID = courseID)


    links = Links.objects.all()
    progress = Progress.objects.filter(userID = userID_id)
    link_progress = list(zip(links,progress))
    for i in links:
        print(i.linksID)
    for j in progress:
        print(j.notes)
    for i,j in link_progress:
        print(i.linksID,j.progressID, j.isCompleted)

    context = {"degreeID": degreeID_id, "course": courses, "topics": topics, "links": links, "link_progress": link_progress} 
    print(progress)

    return render(request,'seniorProjectApp/links.html',context)


def progress(request,userID_id,degreeID_id,courseID,linksID, progressID):
    #testUser = 1
    courses = Courses.objects.get(courseID = courseID)
    topics = Topics.objects.filter(courseID = courseID)

    user =  CustomUser.objects.get(id = userID_id)
    progress = Progress.objects.get(userID_id = userID_id,linkID_id = linksID,progressID = progressID)
    link = Links.objects.get( linksID = linksID)
    context = {"user" : user, "degreeID": degreeID_id,"course": courses, "topics": topics, "link": link, "progress": progress} 

    if request.method == 'POST':
        print("got a post request")
        #instance = get_object_or_404(Progress,linkID = linksID)
        form = ProgressForm(request.POST,instance = progress)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            print("form got saved")
            context["form"] = form
            
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'),'seniorProjectApp/progress.html',context)
    else:
        print("Form did not get saved")
        form = ProgressForm(instance = progress)
    context["form"] = form
        


    return render(request,'seniorProjectApp/progress.html',context)
