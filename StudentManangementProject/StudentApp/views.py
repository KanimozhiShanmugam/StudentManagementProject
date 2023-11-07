from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect

from StudentApp.models import City, Course, Student


# Create your views here.
def log_fun(request):
    return render(request,'login.html',{'data':''})

def logdata_fun(request):
    user_name=request.POST['txtuname']
    password=request.POST['txtpasswod']
    user1=authenticate(username=user_name,password=password)
    if user1 is not None:
        if user1.is_superuser:
            return redirect('home')
        else:
            return render(request,'login.html',{'data':'!!User is not superuser!!'})
    else:
        return render(request,'login.html',{'data':'!!Enter proper UserName and Password!!'})
    # if User.objects.filter(is_superuser=True).filter(Q(username=user_name) & Q(password=password)):
    #     return render(request,'home.html',{'data':''})
    # else:
    #     return render(request,'login.html', {'data': '!!UserName not exists!!'})

def register_fun(request):
    return render(request,'register.html',{'data':''})


def regdata_fun(request):
    user_name=request.POST['txtuname']
    user_email=request.POST['txtemail']
    password=request.POST['txtpasswod']
    if User.objects.filter(Q(username=user_name) | Q(email=user_email)).exists():
        return render(request, 'register.html',{'data':'!!UserName and Email is already exists!!'})
    else:
        u1=User.objects.create_superuser(username=user_name,email=user_email,password=password)
        u1.save()
        return redirect('log')


def home_fun(request):
    return render(request,'home.html')


def addstudent_fun(request):
    city=City.objects.all()
    course = Course.objects.all()
    return render(request,'addstudent.html',{'city_data':city,'course_data':course})


def readdata_fun(request):
    s1=Student()
    s1.Student_Name=request.POST['txtname']
    s1.Student_Age = request.POST['txtage']
    s1.Student_Phno = request.POST['txtphno']
    s1.Student_City = City.objects.get(City_Name=request.POST['ddlcity'])
    s1.Student_Course =Course.objects.get(Course_Name=request.POST['ddlcourse'])
    s1.save()
    return redirect('add')


def display_fun(request):
    s1=Student.objects.all()
    return render(request,'display.html',{'data':s1})


def update_fun(request,id):
    s1 = Student.objects.get(id=id)
    city=City.objects.all()
    course=Course.objects.all()
    if request.method=='POST':
        s1.Student_Name = request.POST['txtname']
        s1.Student_Age = request.POST['txtage']
        s1.Student_Phno = request.POST['txtphno']
        s1.Student_City = City.objects.get(City_Name=request.POST['ddlcity'])
        s1.Student_Course = Course.objects.get(Course_Name=request.POST['ddlcourse'])
        s1.save()
        return redirect('dis')
    else:
        return render(request,'update.html',{'data':s1,'city_data':city,'course_data':course})


def delete_fun(request,id):
    s1=Student.objects.get(id=id)
    s1.delete()
    return redirect('dis')


def log_out_fun(request):
    return redirect('log')