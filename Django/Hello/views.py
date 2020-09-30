from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def index(request):
#     return HttpResponse("hello!")

def index(request):
    return render(request, "Hello/index.html")

def dheeraj(request):
    return HttpResponse("hello dheeraj !")

def neha(request):
    return HttpResponse("Hello Neha !")

# def greet(request, name):
#     return HttpResponse(f"hello {name.capitalize()} !")  #alternate to above functions

def greet(request, name):
    return render(request, "hello/greet.html",{
        "name" : name.capitalize()
    })