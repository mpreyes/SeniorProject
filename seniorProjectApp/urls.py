from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('<int:degreeID_id>/', views.dashboard, name='dashboard'),
    # path('links/', views.links, name='links'),
    path('<int:degreeID_id>/<int:courseID>/', views.links, name='links'),
    
]