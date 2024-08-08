from rest_framework import serializers
from .models import Empresas, Usuarios, Valoraciones, Estrellas, Comentarios, AgenciasLima, Departamentos, Distritos, Provincias


# Serializa la tabla Empresas
class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
        fields = '__all__'
    # Solo campos específicos
class EmpresaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
        fields = ['id','logo', 'nombre', 'sede_principal', 'descripcion', 'sitio_web']


# Serializa la tabla valoracion
class ValoracionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Valoraciones
        fields = '__all__'

    # Solo campos específicos
class ValoracionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valoraciones
        fields = ['id', 'puntualidad', 'seguridad', 'economica', 'amabilidad', 'caro', 'inseguro', 'impuntual', 'poco_amables']


# Serializa la tabla Estrellas
class EstrellasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Estrellas
        fields = '__all__'

    # Solo campos específicos
class EstrellaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estrellas
        fields = ['id', 'estrella_1', 'estrella_2', 'estrella_3', 'estrella_4', 'estrella_5']

# Serializa la tabla Usuarios
class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'

class UsuarioDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ['id', 'foto_usuario', 'nombre', 'email']


# Serializa la tabla Comnetarios
class ComentariosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comentarios
        fields = '__all__'

class ComentariosDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentarios
        fields = ['id', 'comentario']


# Serializa la tabla Agenciaslima
class AgenciasLimaSerializers(serializers.ModelSerializer):
    class Meta: 
        model = AgenciasLima
        fields = '__all__'

    # Solo campos específicos
class AgenciaslimaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgenciasLima
        fields = ['id', 'nombre_referencial', 'foto', 'direccion', 'link_mapa', 'horario_de_atencion', 'telefono', 'cochera']


# Serializa la tabla Departamentos
class DepartamentosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Departamentos
        fields = '__all__'


# Serializa la tabla Provincias
class ProvinciasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Provincias
        fields = '__all__'

class ProvinciasDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincias
        fields = ['id', 'nombre']  # Solo campos específicos


# Serializa la tabla Distritos
class DistritosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Distritos
        fields = '__all__'

class DistritosDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distritos
        fields = ['id', 'nombre']  # Solo campos específicos