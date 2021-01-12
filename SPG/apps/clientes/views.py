from django.conf import settings
from django.contrib import messages
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.db import connection
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView




def home(request):
    return render(request, 'base.html', {})

class PaqueteCrear(SuccessMessageMixin, CreateView):
    model = Paquete
    form_class = PaqueteForm
    success_message = 'Paquete creado con exito'

    def get_context_data(self, **kwargs):
        context = super(PaqueteCrear, self).get_context_data(**kwargs)
        context['usuario'] = self.request.user
        schema = connection.schema_name
        context['tenant'] = Tenant.objects.get(schema_name=schema)
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy("clientes:paquete_crear")

def tenant_crear(request):
    schema = connection.schema_name
    usuario = request.user
    public = Tenant.objects.get(schema_name=schema)
    form = TenantForm()
    if request.method == 'POST':
        form = TenantForm(request.POST)
        if form.is_valid():
            try:
                """
                La operación se maneja como transaccional dado que involucra la creación de más de un objeto los cuales
                estan relacionados
                """
                with transaction.atomic():
                    tenant = form.save()
                    """
                    Se crea el dominio y se le asocia información alojada en el tenant. En este punto es que sucede la
                    creación del esquema del tenant en la base de datos
                    """
                    Dominio.objects.create(domain='%s%s' % (tenant.schema_name, settings.DOMAIN), is_primary=True, tenant=tenant)
                    messages.success(request, "El tenant se ha registrado correctamente")
            except Exception:
                messages.error(request, 'Ha ocurrido un error durante la creación del tenant, se abortó la operación')
            return redirect('clientes:tenants_listar')
        else:
            messages.error(request, "Por favor verificar los campos en rojo")
    return render(request, 'clientes/tenant_form.html', {'form': form, 'public': public, 'usuario': usuario})

def tenants_listar(request):
    usuario = request.user
    desactivados = Tenant.objects.filter(estado=False)
    dominios = Dominio.objects.exclude(tenant__schema_name='public').select_related('tenant')
    return render(request, 'clientes/tenant_list.html', {'dominios': dominios, 'usuario': usuario, 'desactivados': desactivados})

def tenant_modificar(request, id_tenant):
    usuario = request.user
    tenant = Tenant.objects.get(id=id_tenant)
    if request.method == 'POST':
        form = TenantForm(request.POST, request.FILES, instance=tenant)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tenant modificada exitosamente!')
            return redirect('clientes:tenants_listar')
        else:
            messages.error(request, 'Por favor corrige los errores')
            return render(request, 'clientes/tenant_form.html', {'form': form, 'usuario': usuario})
    else:
        form = TenantForm(instance=tenant)
        return render(request, 'clientes/tenant_form.html', {'form': form, 'usuario': usuario})

 
def tenant_desactivar(request, id_tenant):
    tenant = Tenant.objects.get(id=id_tenant)
    tenant.estado = False
    tenant.save()
    Dominio.objects.get(tenant_id=id_tenant).delete()
    return redirect('clientes:tenants_listar')


def tenant_activar(request, id_tenant):
    tenant = Tenant.objects.get(id=id_tenant)
    tenant.estado = True
    tenant.save()
    Dominio.objects.create(domain='%s%s' % (tenant.schema_name, settings.DOMAIN), is_primary=True, tenant=tenant)
    return redirect('clientes:tenants_listar')