from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Welcome Home")
# Create your views here.
def register(requst):
    return HttpResponse("Register Here")
