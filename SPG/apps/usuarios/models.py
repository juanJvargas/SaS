from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    telefono = models.CharField(max_length=11)
    cedula = models.CharField(max_length=11, unique=True)
    direccion = models.CharField(max_length=50)
    tenant = models.CharField(max_length=50)
    cargos = (('Gerente', 'Gerente'), ('Vendedor', 'Vendedor'), ('Cliente', 'Cliente'))
    cargo = models.CharField(max_length=9, choices=cargos, default='Gerente')
    REQUIRED_FIELDS = ['first_name', 'last_name', 'cedula', 'email', 'is_active', 'cargo', 'telefono'
                        ,'cargo']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.cedula + ' - ' + self.get_full_name()

    def get_empleados():
        try:
            empleados = User.objects.filter(cargo__in=('Gerente', 'Vendedor'))
            return empleados
        except User.DoesNotExist:
            return None
    

