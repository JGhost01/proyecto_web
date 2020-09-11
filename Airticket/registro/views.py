from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import Template, context, loader


# Create your views here.
def index(request):

    doc = loader.get_template('index.html')
    ver = doc.render({}) 
    return HttpResponse(ver)

def about(request):

    doc = loader.get_template('about.html')
    ver = doc.render({}) 
    return HttpResponse(ver)

def reservar(request):

    doc = loader.get_template('reservar.html')
    ver = doc.render({}) 
    return HttpResponse(ver)

def contac(request):

    doc = loader.get_template('contac.html')
    ver = doc.render({}) 
    return HttpResponse(ver)