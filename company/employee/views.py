from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Get_all_Employee(request):
    return HttpResponse("<h1> hello this is sanket's site </h1>")

def Get_one_Employee(request,id):
    return HttpResponse("<h1> hello this is single employee </h1>")

def edit_Employee(request,id):
    return HttpResponse("<h1> hello this edit </h1>")

def Delete_Employee(request):
    return HttpResponse("<h1> hello this is delete </h1>")