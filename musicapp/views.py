from django.shortcuts import render
from django.http import HttpResponse, httpResponse

# Create your views here.
def index(request):
    return HttpResponse("Yayyyyy")
