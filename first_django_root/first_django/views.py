from django.http import HttpResponse
from django.shortcuts import render


def first_page(request):
    a = "<h1>Hello Dmitry</h1>"
    return render(request,'./templates/index.html')
