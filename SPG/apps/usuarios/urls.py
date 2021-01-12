from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from apps.usuarios.views import *
from apps.usuarios import views

app_name = 'usuarios'
 
urlpatterns = [
    path('login', LoginView.as_view(redirect_authenticated_user=True,
                    template_name='usuarios/login.html'), name='login'),

    path('home', home, name='home'), 
    path('landing-page', landing, name='landing'),
    path('registro', views.Registro.as_view(), name='registro'),
    path('crear-empleado', views.CrearEmpleado.as_view(template_name='usuarios/empleado_crear.html'), name='crear_empleado'),
    path('listar-empleados', views.listar_empleados.as_view(template_name='usuarios/empleado_list.html'), name='listar_empleados'),
    path('ver-empleado/<int:pk>', views.UsuarioDetalle.as_view(template_name='usuarios/empleado_detail.html'), name='empleado_detalle'),
    path('desactivar-usuario/<int:id_usuario>', usuario_desactivar, name='usuario_desactivar'),
    path('activar-usuario/<int:id_usuario>', usuario_activar, name='usuario_activar'),
]
''' 
path('editar/empleado/<int:id_user>', editar_empleado, name='modificar_empleado'),
    path('detalle/empleado/<int:id_user>', detalle_empleado, name='detalle_empleado')
'''