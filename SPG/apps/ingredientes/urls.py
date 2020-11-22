  
from django.urls import path

from apps.ingredientes.views import *

app_name = 'ingredientes'

urlpatterns = [
    path('', GestionIngredientes, name='manage'),


    
]

    """path('add', Add_product, name='add'),
    path('see/<id>', See_product, name='see'),  
    path('edit/<id>', Edit_product, name='edit'),
    path('consult/', Consult_product, name='consult'),"""