from django import forms
from registro.models import Cliente, Vuelo

class form_cliente(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = ("nombre","apellido","telefono","edad")

