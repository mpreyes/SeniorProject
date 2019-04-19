from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

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
    courseLink = models.CharField(max_length=100,default="links/") #is this needed? remove
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
    linkName = models.CharField(max_length=100) #linkName
    #linkUrl = models.CharField(max_length=100, default="Link here")
    topicID = models.ForeignKey(Topics, on_delete=models.CASCADE) 


# class Users(models.Model):
#     userID = models.AutoField(User, primary_key=True,default=999)
#     degreeID = models.IntegerField()


class CustomUser(AbstractUser):
    # userID = models.AutoField(User, primary_key=True,default=999)
    degreeID = models.IntegerField()
    def __str__(self):
        return self.degreeID
        


class Progress(models.Model):
    progressID = models.AutoField(primary_key=True)
    isCompleted = models.BooleanField()
    notes = models.TextField()
    userID = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    linkID = models.ForeignKey(Links, on_delete=models.CASCADE) 


