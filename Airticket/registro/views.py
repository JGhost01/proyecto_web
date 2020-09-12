from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.template import Template, context, loader
from registro.forms import form_cliente
from registro.models import Cliente


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
    if request.method == 'POST':
        form = form_cliente(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservar')
    else:
        form = form_cliente()
    
    return render(request, 'reservar.html', {'form':form})

def contac(request):

    doc = loader.get_template('contac.html')
    ver = doc.render({}) 
    return HttpResponse(ver)

def clientes_view(request):
    client = Cliente.objects.all()
    contexto = {'clientes':client}
    return render(request, 'clientes_view.html', contexto)