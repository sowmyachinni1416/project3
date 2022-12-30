from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sowmya(request):
    return HttpResponse('<h1>sowmya is a good gril</h1>')

def chinni(request):
     return HttpResponse('<d>to see chinni view response</d>')
