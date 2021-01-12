from django.urls import path
from apps.productos import views

#from apps.accounts.decorators import check_recaptcha

app_name = 'productos'

urlpatterns = [
    path('listar-productos', views.ProductosListar.as_view(), name='productos_listar'),
    path('crear-producto', views.ProductoCrear.as_view(), name='producto_crear'),

    path('listar-ingredientes', views.IngredientesListar.as_view(), name='ingredientes_listar'),
    path('crear-ingrediente', views.IngredienteCrear.as_view(), name='ingrediente_crear'),
     

    path('nuestro-menu/', views.Tienda.as_view(template_name='productos/menu.html'), name='menu'),
    path('tienda/', views.Tienda.as_view(template_name='productos/tienda.html'), name='tienda'),
    path('ver-item/<int:pk>', views.Item.as_view(template_name='productos/item.html'), name='item'),
]
