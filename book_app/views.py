from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse("Welcome to Library Management System")

def library_info(request):
    return HttpResponse("Welcome to Our Library")

def book_list(request):
    return HttpResponse("Python, Django, Java, React, MySQL")

def book_details(request):
    return HttpResponse("Book Name: Django | Author: William S. Vincent")

def contact_info(request):
    return HttpResponse("Contact us at library@gmail.com")
