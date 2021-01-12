from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.hashers import make_password
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.db import connection
from django.urls import reverse_lazy


from apps.usuarios.forms import *
from apps.usuarios.models import Usuario
from apps.clientes.models import *

 


class Registro(SuccessMessageMixin, CreateView):
    model = Usuario
    fields = ['first_name', 'last_name', 'documento', 'ciudad', 'barrio', 'direccion', 'telefono', 'username', 'email', 'password']

    success_message = "Gracias por registrarte"
    def form_valid(self, form):
        form_data =form.cleaned_data
        try:
            if form_data['password']:
                form.instance.password= make_password(form_data['password'])
        except KeyError:
            pass
        return super(Registro, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(Registro, self).get_context_data(**kwargs)
        schema = connection.schema_name
        context['tenant'] = Tenant.objects.get(schema_name=schema)
        context['usuario'] = self.request.user
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy("usuarios:login")

class CrearEmpleado(SuccessMessageMixin, CreateView):
    model = Usuario
    fields = ['first_name', 'last_name', 'documento', 'ciudad', 'barrio', 'direccion', 'telefono', 'username', 'email',
              'password']

    success_message = "Empleado creado exitosamente"
    def form_valid(self, form):
        form.instance.is_staff = True
        form_data =form.cleaned_data
        try:
            if form_data['password']:
                form.instance.password= make_password(form_data['password'])
        except KeyError:
            pass

        return super(CrearEmpleado, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CrearEmpleado, self).get_context_data(**kwargs)
        context['usuario'] = self.request.user
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy("usuarios:listar_empleados")


class listar_empleados(ListView):
    model = Usuario

    def get_queryset(self):
        return Usuario.objects.filter(is_superuser=False, is_staff=True)

    def get_context_data(self, **kwargs):
        context = super(listar_empleados, self).get_context_data(**kwargs)
        context['usuario'] = self.request.user
        return context

class UsuarioDetalle(DetailView):
    model = Usuario

    def get_context_data(self, **kwargs):
        context = super(UsuarioDetalle, self).get_context_data(**kwargs)
        context['usuario'] = self.request.user
        return context


def usuario_desactivar(request, id_usuario):
    usuario = Usuario.objects.get(id=id_usuario)
    usuario.is_active = False
    usuario.save()
    return redirect('usuarios:listar_empleados')

def usuario_activar(request, id_usuario):
    usuario = Usuario.objects.get(id=id_usuario)
    usuario.is_active = True
    usuario.save()
    return redirect('usuarios:listar_empleados')

def home(request):
    usuario = request.user
    return render(request, 'index.html', {})

def landing(request):
    usuario = request.user
    return render(request, 'usuarios/landing_page.html', {})
