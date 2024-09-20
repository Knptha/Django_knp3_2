from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import loader

def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())
