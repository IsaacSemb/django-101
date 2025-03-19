from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# return some html from a render 
def intro (request):
    return HttpResponse('<h1>welcome to the book keeper</h1>')

# returning an entire template
def welcome(request):
    return (render(request, 'welcome.html'))

# returning an template with some logic
def welcome(request):
    name = 'Isaac Ssembuusi'
    return (render(request, 'welcome.html',{'names':name}))