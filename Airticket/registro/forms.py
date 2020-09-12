from django import forms
from registro.models import Cliente

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
