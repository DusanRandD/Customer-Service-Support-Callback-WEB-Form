# Customer-Service-Support-Callback-WEB-Form
The Customer Service Support Callback WEB Form provide customer complain information forward into admin database and schedules callback time from the service department to customer. Admin could also add comments and archive records after completing troubleshooting with possibility for sorting records according to date and time. This application was created in Django and works in virtual environment.

# Installation and setup guide:
<pre>
download zip project
unzip where you want
open command prompt and navigate to unzipped folder<br>

in command prompt type: <br>

<b>pip install virtualenv </b>                 #this will install your virtual environment<br>
<b>virtualenv venv</b>                         #name it<br>
<b>cd venv</b><br>
<b>Scripts\activate</b>                        #this will activate virtual environment, venv is now on the front<br>
<b>pip install django</b>                 	#this will install django<br>
<b>cd..</b><br>
<b>cd mysite</b>                               #enter in mysite forlder<br>
<b>python manage.py test</b>                   #one test is available, not required<br>
<b>python manage.py createsuperuser</b>        #create admin, type: username, email, password(min 8 char)<br>
<b>python manage.py runserver</b>      	#runserver<br><br>

Copy url from console to browser and hit enter. This will load Customer support form.
To load admin page add in browser url /admin , then login with created username and password.<br><br>

Turn off procedure in console:<br>
<b>ctrl+c</b>                                  #stop server<br>
<b>cd..</b><br>
<b>cd venv</b><br>
<b>Scripts\deactivate</b>                      # stop virtual environment<br>
</pre>
