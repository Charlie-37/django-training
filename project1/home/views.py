from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    context = {
        'title': 'Hello, Jinja in Django!', 
        'user_authenticated': True, 
        'username': 'GeeksforGeeks', 
        'items': ['C/C++', 'Java', 'Python', 'Javascript']
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'service.html')

def contact(request):
    return render(request,'contact.html')