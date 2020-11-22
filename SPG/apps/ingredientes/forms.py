from django import forms

from apps.ingredientes.models import *


class Form(forms.ModelForm):
    
    class Meta:
        model = Ingredientes 
        fields = ("nombre", "descripcion", "is_active")
