from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def chakri(request):
    return HttpResponse('he is very good boy')

def chinna(request):
    return HttpResponse('to view chinna response')

