from django.urls import path
from apps.productos import views

#from apps.accounts.decorators import check_recaptcha

app_name = 'productos'

urlpatterns = [
    path('listar-ingredientes', views.IngredientesListar.as_view(), name='ingredientes_listar'),
    path('crear-ingrediente', views.IngredienteCrear.as_view(), name='ingrediente_crear'),
     
]
