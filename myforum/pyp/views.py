from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth import authenticate

def index(request):
    #your stuff goes here
    return render(request,'pyp/index.html')