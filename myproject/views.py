from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    #return HttpResponse("Welcome Home")
    return render(request,'home.html')
def about(request):
    #return HttpResponse("Welcome to About")
    return render(request,'about.html')

