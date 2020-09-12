# django notes

1. django-admin startproject messagebox : starts project message box
    A. sets up a folder called messagebox that contains:
        i. manage.py file that contains commands for admin functions
        ii. messagebox directory that contains:
            a. asgi.py : sync web servers as wsgi but "new"
            b. setting.py : core values for the framework
            c. urls.py: stores urls used for the web server
            d. wsgi.py : sync web servers "older"

2. python manage.py runserver starts the django web server (ignore updates if sqlite is not needed.) runs on localhost:8000
    A. one can specify another port by adding url:port to the command


3. A Django app is a fully self contained app with its own presentation and controls.
4. To start an app use "python manage.py startapp main (name of app)"


to setup a database using the prescribed default settings in settying.py, use the models.py in the app folder to set up tables and create entries

to execute the structure use the python manage.py makemigrations to migrate to the DB
the python manage.py migrate will execute the commands to the database.
DB inspection is done using the python manage.py inspectdb command

Use the admin paths to run the email app. Set up a super user using manage.py createsuperuser


 

