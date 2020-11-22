from django.db import models


class Ingredientes():
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    
    REQUIRED_FIELDS = ['nombre']

    def __str__(self):
        return self.nombre

    

