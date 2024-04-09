from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello World")

def world(request):
    return HttpResponse(" World")

def indexf(request):
    dict = {
        'firstname':'sam',
        'lastname' : 'bahadur',
        'salary' : '12000'
    }
    return render (request,'index.html',dict)
