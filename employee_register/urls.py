from django.urls import path, include
from .import views
urlpatterns = [
    path('', views.employee_form),
    path('list/', views.employee_list),
    path('test/', views.test),

]