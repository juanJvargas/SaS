from django.shortcuts import render
from apps.productos.models import *
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.db import connection
from apps.clientes.models import *
from .forms import *
# Create your views here.



class IngredientesListar(ListView):
    model = Ingrediente

    def get_context_data(self, **kwargs):
        context = super(IngredientesListar, self).get_context_data(**kwargs)
        context['usuario'] = self.request.user
        schema = connection.schema_name
        context['tenant'] = Tenant.objects.get(schema_name=schema)
        return context


class IngredienteCrear(SuccessMessageMixin, CreateView):
    model = Ingrediente
    fields = '__all__'
    success_message = 'Ingrediente agregado con exito'

    def get_context_data(self, **kwargs):
        context = super(IngredienteCrear, self).get_context_data(**kwargs)
        context['usuario'] = self.request.user
        schema = connection.schema_name
        context['tenant'] = Tenant.objects.get(schema_name=schema)
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy("productos:ingredientes_listar")

