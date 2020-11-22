from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
import json
from django.contrib import messages
from django.contrib.auth.decorators import login_required



@login_required
def Manage_products(request):
	
	return render(request, 'gestion_product.html',
					{'products': Producto.get_info()})


#@login_required
def Add_product(request):
	if(request.method == 'POST'):
		form = Product_form(request.POST, request.FILES)
		if form.is_valid():
			productos = form.save()
			productos.save()
			return redirect('/productos')
		else:
			messages.error(request, 'Por favor corrige los errores')
			context = {
			'form': form,
			}
			template = loader.get_template('add_product.html')
			return HttpResponse(template.render(context, request))
	else:
		
		form = Product_form()
		template = loader.get_template('add_product.html')
		context = {
			'form': form,
		}
		return HttpResponse(template.render(context, request))

