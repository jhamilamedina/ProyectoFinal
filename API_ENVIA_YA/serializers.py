from rest_framework import serializers
from .models import Empresa, Usuario, Valoracion, Estrella, Comentario, AgenciaLima, Departamento, Distrito, Provincia

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class ValoracionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Valoracion
        fields = '__all__'

class EstrellasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Estrella
        fields = '__all__'

class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ComentariosSerializers(serializers.ModelSerializer):
    class Meta:
        models = Comentario
        fields = '__all__'

class AgenciasLimaSerializers(serializers.ModelSerializer):
    class Meta: 
        models = AgenciaLima
        fields = '__all__'

class DepartamentosSerializers(serializers.ModelSerializer):
    class Meta:
        models = Departamento
        fields = '__all__'

class ProvinciasSerializers(serializers.ModelSerializer):
    class Meta:
        models = Provincia
        fields = '__all__'

class DistritosSerializers(serializers.ModelSerializer):
    class Meta:
        models = Distrito
        fields = '__all__'