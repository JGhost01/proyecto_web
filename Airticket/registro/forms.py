from django import forms
from registro.models import Cliente, Vuelo

class form_cliente(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = [
            "nombre",
            "apellido",
            "telefono",
            "edad",
            
        ]

        labels = {
            "nombre":"Nombre",
            "apellido":"Apellido",
            "telefono":"Telefono",
            "edad":"Edad",
        }

        widget = {
            "nombre": forms.TextInput(attrs={"class":"form-control"}),
            "apellido": forms.TextInput(attrs={"class":"form-control"}),
            "telefono": forms.TextInput(attrs={"class":"form-control"}),
            "edad": forms.NumberInput(attrs={"class":"form-control"}),
        }

class form_vuelo(forms.ModelForm):
    
    class Meta:
        model = Vuelo
        fields = [
            "tipo_vuelo",
            "clase",
            "origen",
            "destino",
            "fecha_salida",
            "fecha_regreso",
            "clientes"
            
        ]

        labels = {
            "tipo_vuelo":"Tipo",
            "clase":"Clase",
            "origen":"Origen",
            "destino":"Destino",
            "fecha_salida":"Fecha de Salida",
            "fecha_regreso":"Fecha de Regreso",
            "clientes":"Cliente",
        }

        widget = {
            "tipo_vuelo": forms.Select(attrs={"class":"form-control"}),
            "clase": forms.Select(attrs={"class":"form-control"}),
            "origen": forms.TextInput(attrs={"class":"form-control"}),
            "destino": forms.TextInput(attrs={"class":"form-control"}),
            "fecha_salida": forms.TextInput(attrs={'type': 'date'}),
            "fecha_regreso": forms.TextInput(attrs={'type': 'date'}),
            "clientes": forms.Select(attrs={"class":"form-control"}),
        }
