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

def contac(request):

    doc = loader.get_template('contac.html')
    ver = doc.render({}) 
    return HttpResponse(ver)

def reservar(request):
    if request.method == 'POST':
        form = form_cliente(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'reservar.html', {'form':form, 'mensaje':'OK'})
    else:
        form = form_cliente()
    
    return render(request, 'reservar.html', {'form':form})

def clientes_view(request):
    client = Cliente.objects.all()
    contexto = {'clientes':client}
    return render(request, 'clientes_view.html', contexto)

def clientes_edit(request, id_cliente):
    client = Cliente.objects.filter(id=id_cliente).first()
    form = form_cliente(instance=client)
    return render(request, 'clientes_edit.html', {'form':form, 'cliente':client})

def clientes_update(request, id_cliente):
    client = Cliente.objects.get(pk=id_cliente)
    form = form_cliente(request.POST, instance=client)
    if form.is_valid():
        form.save()
    client = Cliente.objects.all()
    return redirect('clientes_view')

def clientes_delete(request, id_cliente):
    client = Cliente.objects.get(id=id_cliente) 
    if  request.method == 'POST':
        client.delete()
        return redirect('clientes_view')
    return render(request, 'clientes_delete.html', {'clientes':client})

