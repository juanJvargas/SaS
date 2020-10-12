from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from apps.usuarios.forms import SignUpForm
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
    