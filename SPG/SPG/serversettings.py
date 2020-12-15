
DBCONFIG = {}
DBCONFIG['default'] = {
    'ENGINE': 'django_tenants.postgresql_backend',
    'NAME': 'SaaS',
    'USER': 'postgres',
    'PASSWORD': 'admin',
    'HOST': 'localhost',
    'PORT': 5433, 
}
'''
import dj_database_url
from decouple import config

DBCONFIG ={
    'default': dj_database_url.config(
        default = config('DATABASE_URL')
    )
}
'''