from django.urls import path, include
from .import views
urlpatterns = [
    path('', views.employee_form, name='employee_insert'), #insert data
    path('<int:id>/', views.employee_form, name='employee_update'), #edit information
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'), #delete 
    path('list/', views.employee_list, name='employee_list'), #display record
    path('test/', views.test),
    path('time/', views.time),

]