from django.urls import path, include # new
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('<int:degreeID_id>/', views.dashboard, name='dashboard'),
    path('<int:degreeID_id>/<int:courseID>/', views.links, name='links'),
    path('<int:degreeID_id>/<int:courseID>/<int:linksID>/', views.progress, name='links'),
    
    
]