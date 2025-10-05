from rest_framework import serializers
from .models import Empresa


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = [
            'IdEmpresa','Empresa','RFC','Calle','Colonia','CP','IdPais','IdEstado',
            'IdMunicipio','Comentario','IdEstatus','UsuarioOwnerIngreso','FechaIngreso','CodigoEmpresa'
        ]