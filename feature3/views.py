from django.shortcuts import render
from django.http import HttpResponse
def rose(request):
    return HttpResponse('<h1>my rose for u</h1>')


# Create your views here.
