from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.usuarios.urls')),
    path('clientes/', include('apps.clientes.urls', namespace='clientes')),
    path('auth', include('social_django.urls', namespace='social')),
    path('select2/', include('django_select2.urls')),
    
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)