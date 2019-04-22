from django.urls import path, include # new
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('redirectme/', views.redirectme, name='redirectme'),
    path('<int:userID_id>/<int:degreeID>/', views.dashboard, name='dashboard'),
    path('<int:userID_id>/<int:degreeID_id>/<int:courseID>/', views.links, name='links'),
    path('<int:userID_id>/<int:degreeID_id>/<int:courseID>/<int:linksID>/<int:progressID>/', views.progress, name='links'),
    
    
]