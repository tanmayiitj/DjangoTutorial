from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def success_page(request):
    return HttpResponse("Hey again fucker!!")
def home(request):
    people = [
        {'name':'Tanmay', 'age':22},
        {'name':'Priyanshu', 'age':22},
        {'name':'Shahzen', 'age':23},
        {'name':'Rohit', 'age':20},
        {'name':'Piyush', 'age':23},
        {'name':'Pulkit', 'age':22},
    ]

    return render(request,"index.html",context={'peoples':people})