from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'home.html')


def add(request):
    first = int(request.POST["num1"])
    second = int(request.POST["num2"])
    res = first + second
    return render(request, "result.html", {'result': res})
