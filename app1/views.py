from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def naveen(request):
    return HttpResponse ('Natural Star') 
def sekhar(request):
    return HttpResponse('<h1>this is the second view inapp1</h1>')