from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def intro ():
    return HttpResponse('<h1>welcome to the book keeper</h1>')