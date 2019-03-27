from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Ye olde Database models.


#Computer Science

class Degree(models.Model):
    degreeID = models.AutoField(primary_key=True)
    degreeName = models.CharField(max_length=60)
    


#Intro to programming

class Courses(models.Model):
    courseID = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=100)
    courseDescription = models.CharField(max_length=400,default="default description")
    courseLink = models.CharField(max_length=100,default="links/")
    degreeID = models.ForeignKey(Degree, on_delete=models.CASCADE) 
    level = models.CharField(max_length=50,default="Freshman")
    


#Loops
class Topics(models.Model):
    topicID = models.AutoField(primary_key=True)
    topicName = models.CharField(max_length=100)
    courseID = models.ForeignKey(Courses, on_delete=models.CASCADE) 
    


#Link to Geeks2Geeks article on loops
class Links(models.Model):
    linksID = models.AutoField(primary_key=True)
    linkName = models.CharField(max_length=100)
    topicID = models.ForeignKey(Topics, on_delete=models.CASCADE) 


class Users(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE,default=999)
    #userID = models.AutoField(primary_key=True)
    degreeID = models.IntegerField()


class Progress(models.Model):
    progressID = models.IntegerField(primary_key=True)
    isCompleted = models.BooleanField()
    notes = models.TextField()
    userID = models.ForeignKey(Users, on_delete=models.CASCADE)
    linkID = models.ForeignKey(Links, on_delete=models.CASCADE) 


