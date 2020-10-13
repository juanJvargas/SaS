from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from apps.usuarios.forms import SignUpForm, EditarEmpleado, EditarEmpleadoExtra
from apps.usuarios.models import User
from django.contrib import messages

def listar_empleados():
    return User.get_empleados()

def signup(request):
    # Usuario que hizo la peticion a la funcion (usuario que esta en la sesion)
    #usuario = request.user
    # Validacion para cuando el administrador (is_staff)
    #if usuario.is_staff or True:
    if True: 
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            #if form.is_valid() and user_data.is_valid() and request.recaptcha_is_valid:
            if form.is_valid():
                #messages.success(request, 'Empleado registrado exitosamente')

                user = form.save(commit=False)
                user.save()

                return render(request, 'usuarios/signup.html',
                              {'form': SignUpForm(), 'empleados': listar_empleados()})
            else:
                #messages.error(request, 'Por favor corrige los errores')
                return render(request, 'usuarios/signup.html', {'form': form, 'empleados': listar_empleados()})
        else:
            form = SignUpForm()
            return render(request, 'usuarios/signup.html',
                          {'form': form, 'empleados': listar_empleados()})
    # En caso de que el usuario no sea admin se redirije al home y se muestra mensaje de error
    else:
        messages.error(request, 'No estas autorizado para realizar esta acción')
        return redirect('usuarios:home')



def home(request):
    usuario = request.user
    return render(request, 'index.html', {})

def editar_empleado(request, id_user):
    user = User.objects.get(id=id_user)
    usuario = request.user
    #Quitar el or true cuando se deje lsito el login 
    if usuario.is_staff or True:
        if request.method == 'POST':
            form = EditarEmpleado(request.POST, instance=user)
            form_empleado_extra = EditarEmpleadoExtra(request.POST, instance=user)
            if form.is_valid() and form_empleado_extra.is_valid():
                form.save()
                form_empleado_extra.save()
                messages.success(request, 'Has modificado el empleado exitosamente!')
                return redirect('usuarios:registro')
            else:
                messages.error(request, 'Por favor corrige los errores')
                return render(request, 'usuarios/editar_empleado.html', {'form': form,
                                                                         'form_empleado_extra': form_empleado_extra})

        else:
            form = EditarEmpleado(instance=user)
            form_empleado_extra = EditarEmpleadoExtra(instance=user)
            return render(request, 'usuarios/editar_empleado.html', {'form': form,
                                                                     'form_empleado_extra': form_empleado_extra})

    else:
        messages.error(request, 'No estas autorizado para realizar esta acción')
        return redirect('usuarios:home')
