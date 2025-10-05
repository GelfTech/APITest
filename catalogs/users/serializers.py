from rest_framework import serializers
from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'IdRegistro','IdEmpresa','IdUsuario','Passwd','TipoUsuario',
            'NombreUsuario','Email','IdEstatus','UsuarioOwnerIngreso',
            'UsuarioIngreso','FechaIngreso'
        ]
        extra_kwargs = { 'Passwd': {'write_only': True} }

    def validate(self, attrs):
        if attrs.get('UsuarioOwnerIngreso') and attrs.get('UsuarioIngreso'):
            raise serializers.ValidationError('UsuarioOwnerIngreso y UsuarioIngreso no pueden coexistir.')
        return attrs