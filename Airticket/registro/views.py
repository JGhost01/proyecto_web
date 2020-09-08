from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, context, loader

# Create your views here.
def index(request):

    doc = loader.get_template('index.html')
    ver = doc.render({}) 
    return HttpResponse(ver)
