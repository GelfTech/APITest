from django.db import models


class Empresa(models.Model):
    IdEmpresa = models.IntegerField(primary_key=True, db_column='IdEmpresa')
    Empresa = models.CharField(max_length=50, db_column='Empresa')
    RFC = models.CharField(max_length=50, db_column='RFC')
    Calle = models.CharField(max_length=50, db_column='Calle', null=True, blank=True)
    Colonia = models.CharField(max_length=50, db_column='Colonia', null=True, blank=True)
    CP = models.IntegerField(db_column='CP', null=True, blank=True)
    IdPais = models.IntegerField(db_column='IdPais', null=True, blank=True)
    IdEstado = models.IntegerField(db_column='IdEstado', null=True, blank=True)
    IdMunicipio = models.IntegerField(db_column='IdMunicipio', null=True, blank=True)
    Comentario = models.CharField(max_length=200, db_column='Comentario', null=True, blank=True)
    IdEstatus = models.IntegerField(db_column='IdEstatus', default=1)
    UsuarioOwnerIngreso = models.CharField(max_length=20, db_column='UsuarioOwnerIngreso', null=True, blank=True)
    FechaIngreso = models.DateTimeField(db_column='FechaIngreso', null=True, blank=True)
    CodigoEmpresa = models.CharField(max_length=6, db_column='CodigoEmpresa')


    class Meta:
        managed = False
        db_table = '"General.Empresa"'