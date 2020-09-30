from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name= "index"),
    path("dheeraj", views.dheeraj, name ="dheeraj"),
    path("neha", views.neha, name = "neha"),
    path("<str:name>", views.greet, name = "greet")
]
#what views urls are to be used