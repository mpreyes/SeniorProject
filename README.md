Senior Seminar Project 2019, Lipscomb University 

CodeMentor is web application that is made up of a collection of 
resources designed to assist students at Lipscomb University who 
want to learn topics taught in computing coursework in preparation 
for college or review topics from their time in college before they graduate. 

The site is currently a working prototype.


![Code Mentor Frontend](https://github.com/mpreyes/SeniorProject/blob/master/seniorProjectApp/static/seniorProjectApp/img/indexscreenshot.png)


Written in Django, (2.0.2) HTML/CSS, SQL, Bootstrap 3.37.


Use python3 for all commands to avoid confusion.

To run the development server:

python3 manage.py runserver

The index page introduces the goals of the site and highlights research and potential course offerings. 

Users can create a new account using the Sign Up button in the navigation. 
Then they are able to log in using the Log in button. After logging in, users are redirected to a 
dashboard that shows them the computing courses required in the degree they chose when they signed up. 

![Code Mentor Frontend](https://github.com/mpreyes/SeniorProject/blob/master/seniorProjectApp/static/seniorProjectApp/img/dashboardscreenshot.png)

On the dashboard, courses are separated by level (freshman, sophomore, junior, senior). Each course 
has a description, and when a user clicks on a course, they are directed to the links page for that 
specific course. 

![Code Mentor Frontend](https://github.com/mpreyes/SeniorProject/blob/master/seniorProjectApp/static/seniorProjectApp/img/linksscreenshot.png)

The links page includes topics taught in the course and resources for each topic. 
For each resource, there is a progress star that indicates whether the user has completed that link 
and a note-taking feature. When users click on the Notes button, they are taken to another page that 
allows them to take notes and edit previous notes as well as mark the link as complete, which will 
fill in the star for that resource on the links page. 

![Code Mentor Frontend](https://github.com/mpreyes/SeniorProject/blob/master/seniorProjectApp/static/seniorProjectApp/img/notesscreenshot.png)

Users must click the Save Changes button for changes to be saved. They can return to the links page for the course they were working on by using the Back button. 

Users can navigate back to their dashboard by clicking the Dashboard link in the navigation. 

 
