## README

**SQL para Tenants**

`INSERT INTO "tenants_tenant" ("schema_name", "nombre", "direccion", "telefono","pagado_hasta","estado") VALUES
('public', 'public','Cll 100 #12-03','5555555', '2099-01-01','True');`

`INSERT INTO "tenants_dominio" ("domain", "is_primary", "tenant_id") VALUES
('127.0.0.1', true, 1);`

`INSERT INTO "tenants_estilos" ("nombre") VALUES ('Basico');`
`INSERT INTO "tenants_estilos" ("nombre") VALUES ('Medio');`
`INSERT INTO "tenants_estilos" ("nombre") VALUES ('Profesional');`


**NOTA:** Debe crearse un superuser para cada tenant el cual será su administrador

python manage.py tenant_command createsuperuser --schema="[Nombre del tenant]"

**IMPORTAR cities a cada Tenant**
`python manage.py tenant_command loaddata cities_light_country.json --schema="[Nombre del tenant]"`

`python manage.py tenant_command loaddata cities_light_region.json --schema="[Nombre del tenant]"`

`python manage.py tenant_command loaddata cities_light_city.json --schema="[Nombre del tenant]"`


