# Django-CRUD project for employee project


Django CRUD operstion.

1)	Create django project 
Creating virtual environment-(cmd)
•	python -m venv venv
•	ven\Scripts\activate
•	pip install django
•	django-admin startproject employee_project(name of my project)
change directory to employee_project to run project then 
•	python manage.py runserver
 
2)	Create app in this project
•	Python manage.py startapp employee_register
Go to employee_project setting.py and add employee_register in installed app

3)	Create database with postgress
•	Crate data base using name (postgree app)
Back to employee_project setting.py
•	import psycopg2


•	DATABASES = {
•	    'default': {
•	        'ENGINE': 'django.db.backends.postgresql',
•	        'NAME': name,
•	        'USER': 'postgres',
•	        'PASSWORD': 'emon',
•	        'HOST': 'localhost',
•	        'PORT':'5432',
•	    }
•	}

•	Python manage.py migrate

 
Done database connection
4)	Create model on employee_register models.py file
from turtle import position
from django.db import models

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=50)

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)

Make migrations
•	python manage.py makemigrations employee_register
•	python manage.py sqlmigrate employee_register 0001 (modification)
•	python manage.py migrate (to apply migration)

5)	employee_register -> views.py
Create some function to view 
def employee_list(request):
    return

def employee_form(request):
    return

def employee_delete(request):
    return

6)	employee_project -> urls.py
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', include('employee_register.urls'))
]


7)	employee_register -> create urls.py
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.employee_form),
    path('list/', views.employee_list),
]

#Template Section:
Create a folder name template in employee_register folder. Add another folder to template name will be same as employee_register.
Then create html file in employee_register folder
•	base.html
•	 {% block content %}
•	
•	    {% endblock content %}
Use this in body section
•	Employee_list
•	{% extends "employee_register/base.html" %}
•	
•	{% block content %}
•	
•	<p>We will show employee list</p>
•	{% endblock content %}

•	Employee_form
{% extends "employee_register/base.html" %}

{% block content %}

<p>We will show employee form</p>
{% endblock content %}



Now design part of base html.



8)	Form

•	Create from.py in employee_register
from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    
    class Meta:

        model = Employee
        fields = '__all__'

•	Add this code on views.py

from .forms import EmployeeForm

def employee_form(request):
    form = EmployeeForm()
    return render(request, "employee_register/employee_form.html", {'form':form})

•	Use this in form html page
{{form}}


Output like this

 
	




