from django.urls import path

from StudentApp import views

urlpatterns = [
    path('',views.log_fun,name='log'),#it will diplay login.html page
    path('logdata',views.logdata_fun),#it will read data and check whether it is superuser or not
    path('reg',views.register_fun,name='reg'),#it will redirect to register.html page
    path('regdata',views.regdata_fun),#it will create a superuser account
    path('home',views.home_fun,name='home'),
    path('add_students',views.addstudent_fun,name='add'),
    path('readdata',views.readdata_fun),
    path('display',views.display_fun,name='dis'),
    path('update/<int:id>',views.update_fun,name='up'),
    path('delete/<int:id>',views.delete_fun,name='del'),
    path('log_out',views.log_out_fun,name='log_out')
    ]