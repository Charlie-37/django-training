from django.shortcuts import render, redirect
from .models import Receipe, Student, Department
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.
@login_required(login_url='/vege/login')
def receipes(request):
    if request.method == 'POST':
        receipe_image = request.FILES.get("receipe_image")
        receipe_name = request.POST.get("receipe_name")
        receipe_description = request.POST.get("receipe_description")
        
        Receipe.objects.create(receipe_image=receipe_image,receipe_name = receipe_name,receipe_description = receipe_description)
        
        return redirect('/vege/add_receipes/')
    
    queryset = Receipe.objects.all()
    return render(request,"receipes.html",context={"receipes": queryset})

@login_required(login_url='/vege/login')
def update_receipe(request,id):
    queryset = Receipe.objects.get(id=id)
    if request.method =="POST":
        queryset.receipe_name = request.POST.get("receipe_name")
        queryset.receipe_description = request.POST.get("receipe_description")
        if request.FILES.get("receipe_image"):
            queryset.receipe_image = request.FILES.get("receipe_image")
        queryset.save()
        return redirect('/vege/add_receipes/')   
    return render(request,"update_receipe.html",context={"receipe":queryset})

@login_required(login_url='/vege/login')
def delete_receipe(request,id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/vege/add_receipes/')

def login_page(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username=username):
            messages.info(request,'Wrong Username & Password')
            return redirect('/vege/login')
        
        user = authenticate(username=username, password=password)
        if user is None:
            messages.info(request,'Wrong Username & Password')
            return redirect('/vege/login')
        else:
            login(request,user)
            return redirect('/vege/add_receipes')

    return render(request,"login.html")

def logout_page(request):
    logout(request)
    return redirect('/vege/login')

def register_page(request):
    if request.method != 'POST':
        return render(request,"register.html")
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = User.objects.filter(username=username)
    if user.exists():
        messages.info(request,'Username already taken')
    else:
        user = User.objects.create(first_name=first_name,last_name=last_name,username=username)
        user.set_password(password)
        user.save()
        messages.success(request,'Account Created Successfully')
    return redirect('/vege/register')


def student_page(request):
    return render(request,"student.html")

def student_view_page(request):
    print('called')
    std = Student.objects.all()
    dpt = Department.objects.all()
    context ={
        'student': list(std)
    }
    # print(list(std.values()))
    print(list(dpt.values()))
    
    return JsonResponse({"student":list(std.values()),"dpt":dict(dpt.values())})