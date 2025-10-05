from django.db import models
from django.core.exceptions import ValidationError


class Usuario(models.Model):
    IdRegistro = models.AutoField(primary_key=True, db_column='IdRegistro')
    IdEmpresa = models.IntegerField(db_column='IdEmpresa')
    IdUsuario = models.CharField(max_length=50, db_column='IdUsuario')
    Passwd = models.CharField(max_length=200, db_column='Passwd')
    TipoUsuario = models.CharField(max_length=1, db_column='TipoUsuario') # 'A','D','G','S'
    NombreUsuario = models.CharField(max_length=120, db_column='NombreUsuario', null=True, blank=True)
    Email = models.CharField(max_length=120, db_column='Email', null=True, blank=True)
    IdEstatus = models.IntegerField(db_column='IdEstatus', default=1)
    UsuarioOwnerIngreso = models.CharField(max_length=50, db_column='UsuarioOwnerIngreso', null=True, blank=True)
    UsuarioIngreso = models.CharField(max_length=50, db_column='UsuarioIngreso', null=True, blank=True)
    FechaIngreso = models.DateTimeField(db_column='FechaIngreso', null=True, blank=True)


    class Meta:
        managed = False
        db_table = '"Empresa.Usuario"' # o '"Empresa"."Usuario"' si es esquema.tabla
        unique_together = (('IdEmpresa', 'IdUsuario'),)


    def clean(self):
        if self.UsuarioOwnerIngreso and self.UsuarioIngreso:
            raise ValidationError('UsuarioOwnerIngreso y UsuarioIngreso no pueden coexistir.')  