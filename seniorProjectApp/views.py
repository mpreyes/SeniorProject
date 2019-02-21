from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'seniorProjectApp/index.html')


def signup(request):
    return render(request,'seniorProjectApp/signup.html')

def dashboard(request):
    #add any field you want passed to the dashboard.html page
    classes_list = [{"name": "intro to programming", "color": "blue", "link" :"in_prog"},{"name": "class2", "color": "blue"},{"name": "class3", "color": "blue"},{"name": "class4", "color": "blue"}, {"name": "class5", "color": "blue"},{"name": "class6", "color": "blue"}]
    context ={"classes_list": classes_list}
    #print("context " + str(context["classes_list"]))

    return render(request,'seniorProjectApp/dashboard.html',context)

def links(request):
    return render(request,'seniorProjectApp/links.html')

