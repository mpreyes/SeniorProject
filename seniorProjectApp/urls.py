from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # path('links/', views.links, name='links'),
    path('<int:course_id>/', views.links, name='links'),
    
]