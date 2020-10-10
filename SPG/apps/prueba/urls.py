from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from apps.prueba.views import *

app_name = 'prurba'

urlpatterns = [
    path('', auth_views.LoginView.as_view(redirect_authenticated_user=True,
                    template_name='index.html'), name='home'),
    
]