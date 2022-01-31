from django.forms import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import context
from employee_register.models import Employee
from .forms import EmployeeForm
#from . forms import EmployeeForm
#from django.forms import EmployeeForm
from .models import Employee
import datetime
 

# Create your views here.

def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employee_register/employee_list.html", context)

def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form':form})
    else:
        if id ==0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')



def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()

    return redirect('/employee/list')

def test(request):
    return render(request, "employee_register/test.html")


def time(request):
    now = datetime.datetime.now()  
    html = "<html><body><h3>Now time is %s.</h3></body></html>" % now  
    return HttpResponse(html)    # rendering the template in HttpResponse

def index(request):
    return render(request, "employee_register/index.html")