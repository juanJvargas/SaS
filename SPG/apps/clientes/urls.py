from django.urls import path
from .views import *


app_name = 'clientes'
urlpatterns = [
    path('crear-paquete', PaqueteCrear.as_view(), name='paquete_crear'),
    path('crear-tenant', tenant_crear , name='tenant_crear'),
    path('listar-tenants', tenants_listar , name='tenants_listar'),
]
 
'''
    path('registrar/', registrar_cliente, name='registrar'),
    path('modificar/<int:id_cliente>/', modificar_cliente, name='modificar'),
'''