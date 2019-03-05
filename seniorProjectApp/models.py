from django.db import models

# Ye olde Database models.


#Computer Science

class Degree(models.Model):
    degreeID = models.AutoField(primary_key=True)
    degreeName = models.CharField(max_length=60)
    


#Intro to programming

class Courses(models.Model):
    courseID = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=100)
    degreeID = models.IntegerField()
    references = models.ForeignKey(Degree, on_delete=models.CASCADE) 
    


#Loops
class Topics(models.Model):
    topicID = models.AutoField(primary_key=True)
    topicName = models.CharField(max_length=100)
    courseID = models.IntegerField()
    references = models.ForeignKey(Courses, on_delete=models.CASCADE) 
    


#Link to Geeks2Geeks article on loops
class Links(models.Model):
    linksID = models.IntegerField(primary_key=True)
    linkName = models.CharField(max_length=100)
    topicID = models.IntegerField()
    references = models.ForeignKey(Topics, on_delete=models.CASCADE) 




class Users(models.Model):
    userID = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=50) #TODO: make this not a char field.
    token = models.CharField(max_length=50)
    degreeID = models.IntegerField()


class Progress(models.Model):
    progressID = models.IntegerField(primary_key=True)
    userID = models.IntegerField()
    linkID = models.IntegerField()
    isCompleted = models.BooleanField()
    notes = models.TextField()
    references = models.ForeignKey(Users, on_delete=models.CASCADE) 

