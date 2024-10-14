from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import Empresas, Valoraciones, Estrellas, Usuarios, AgenciasLima, Comentarios, Departamentos, Provincias, Distritos
from .serializers import EmpresaSerializer, ValoracionSerializers, EstrellasSerializers, UsuarioSerializers, AgenciasLimaSerializers, ComentariosSerializers, DepartamentosSerializers, ProvinciasSerializers, DistritosSerializers
from .serializers import EmpresaDetailSerializer, AgenciaslimaDetailSerializer, DistritosDetailSerializer, ValoracionDetailSerializer, EstrellaDetailSerializer, ComentariosDetailSerializer, UsuarioDetailSerializer, ProvinciasDetailSerializer


class EmpresasAPIView(APIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def get(self, request, id=None, format=None):
        if id:
            empresa = get_object_or_404(Empresas,id=id)
            serializer = EmpresaDetailSerializer(empresa)
            valoraciones = Valoraciones.objects.filter(empresa=empresa)
            estrellas = Estrellas.objects.filter(empresa=empresa)
            comentarios = Comentarios.objects.filter(empresa=empresa)
            agenciaslima = AgenciasLima.objects.filter(empresa=empresa)
            return Response({
                'Empresa': serializer.data,
                'Agencias': AgenciaslimaDetailSerializer(agenciaslima, many=True).data,
                'Valoraciones': ValoracionDetailSerializer(valoraciones, many=True).data,
                'Estrellas': EstrellaDetailSerializer(estrellas, many=True).data,
                'Comentarios': ComentariosDetailSerializer(comentarios, many=True).data
            })
        else:
            empresas = Empresas.objects.all()
            serializer = EmpresaSerializer(empresas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmpresaSerializer(data=request.data)
        if serializer.is_valid():
            empresa = serializer.save()
            mensaje = f'Datos creados con exito, con ID: {empresa.id}'
            return Response({'message': mensaje,'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id=None, format=None):
        empresa = get_object_or_404(Empresas, id=id)
        serializer = EmpresaSerializer(empresa, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos actualizados con exito', 'data': serializer.data, 'id': id}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        empresa = get_object_or_404(Empresas, id=id)
        empresa.delete()
        return Response({'message': 'Datos eliminados con  exito', 'id': id}, status=status.HTTP_204_NO_CONTENT)

class ValoracionesAPIView(APIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def get(self, request, id=None, format=None):
        if id:
            valoracion = get_object_or_404(Valoraciones, empresa=id)
            serializer = ValoracionSerializers(valoracion)
        else:
            valoraciones = Valoraciones.objects.all()
            serializer = ValoracionSerializers(valoraciones, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        empresa_id = request.data.get('empresa')
        usuario_id = request.user.id  # Obtén el ID del usuario autenticado

        try:
            empresa = Empresas.objects.get(id=empresa_id)
        except Empresas.DoesNotExist:
            return Response({'detail': 'Empresa no encontrada.'}, status=status.HTTP_404_NOT_FOUND)

        valoracion, created = Valoraciones.objects.get_or_create(empresa=empresa)
        
        if usuario_id in valoracion.usuarios:
            return Response({'detail': 'Ya has valorado esta empresa.'}, status=status.HTTP_400_BAD_REQUEST)

        if not created:
            # Si ya existe una valoración, actualízala
            valoracion.puntualidad += request.data.get('puntualidad', 0)
            valoracion.seguridad += request.data.get('seguridad', 0)
            valoracion.economica += request.data.get('economica', 0)
            valoracion.amabilidad += request.data.get('amabilidad', 0)
            valoracion.caro += request.data.get('caro', 0)
            valoracion.inseguro += request.data.get('inseguro', 0)
            valoracion.impuntual += request.data.get('impuntual', 0)
            valoracion.poco_amables += request.data.get('poco_amables', 0)
            valoracion.usuarios.append(usuario_id)  # Añade el ID del usuario a la lista
            valoracion.save()
        else:
            # Si es una nueva valoración, guarda el usuario en la lista
            valoracion.usuarios = [usuario_id]
            valoracion.puntualidad = request.data.get('puntualidad', 0)
            valoracion.seguridad = request.data.get('seguridad', 0)
            valoracion.economica = request.data.get('economica', 0)
            valoracion.amabilidad = request.data.get('amabilidad', 0)
            valoracion.caro = request.data.get('caro', 0)
            valoracion.inseguro = request.data.get('inseguro', 0)
            valoracion.impuntual = request.data.get('impuntual', 0)
            valoracion.poco_amables = request.data.get('poco_amables', 0)
            valoracion.save()

        serializer = ValoracionSerializers(valoracion)
        return Response({'message': 'Valoración creada/actualizada con éxito.', 'data': serializer.data}, status=status.HTTP_201_CREATED)

    def put(self, request, id=None, format=None):
        valoracion = get_object_or_404(Valoraciones, empresa=id)
        usuario_id = request.user.id  # Obtén el ID del usuario autenticado

        if usuario_id not in valoracion.usuarios:
            return Response({'detail': 'No has valorado esta empresa.'}, status=status.HTTP_400_BAD_REQUEST)
        
        data = request.data
        valoracion.puntualidad += data.get('puntualidad', 0)
        valoracion.seguridad += data.get('seguridad', 0)
        valoracion.economica += data.get('economica', 0)
        valoracion.amabilidad += data.get('amabilidad', 0)
        valoracion.caro += data.get('caro', 0)
        valoracion.inseguro += data.get('inseguro', 0)
        valoracion.impuntual += data.get('impuntual', 0)
        valoracion.poco_amables += data.get('poco_amables', 0)
        valoracion.save()

        serializer = ValoracionSerializers(valoracion)
        return Response({'message': 'Valoración actualizada con éxito.', 'data': serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, id=None, format=None):
        valoracion = get_object_or_404(Valoraciones, empresa=id)
        usuario_id = request.user.id  # Obtén el ID del usuario autenticado

        if usuario_id not in valoracion.usuarios:
            return Response({'detail': 'No has valorado esta empresa.'}, status=status.HTTP_400_BAD_REQUEST)
        
        valoracion.usuarios.remove(usuario_id)  # Elimina el ID del usuario de la lista
        valoracion.save()
        
        # Si la lista de usuarios está vacía, elimina la valoración
        if not valoracion.usuarios:
            valoracion.delete()
        
        return Response({'message': 'Valoración eliminada con éxito.'}, status=status.HTTP_204_NO_CONTENT)

class EstrellasAPIView(APIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def get(self, request, id=None, format=None):
        if id:
            estrella = get_object_or_404(Estrellas, id=id)
            serializer = EstrellasSerializers(estrella)
        else:
            estrellas = Estrellas.objects.all()
            serializer = EstrellasSerializers(estrellas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        empresa_id = request.data.get('empresa')
        try:
            empresa = Empresas.objects.get(id=empresa_id)
        except Empresas.DoesNotExist:
            return Response({'detail': 'Empresa no encontrada.'}, status=status.HTTP_404_NOT_FOUND)
        
        if Estrellas.objects.filter(empresa=empresa).exists():
            return Response({'detail': 'Ya existe estrellas para esta empresa.'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = EstrellasSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Estrellas creada con éxito.', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id=None, format=None):
        try:
            estrella = Estrellas.objects.get(id=id)
        except Estrellas.DoesNotExist:
            return Response({'detail': 'estrella no encontrada.'}, status=status.HTTP_404_NOT_FOUND)
        
        data = request.data
        estrella.estrella_1 += data.get('estrella_1', 0)
        estrella.estrella_2 += data.get('estrella_2', 0)
        estrella.estrella_3 += data.get('estrella_3', 0)
        estrella.estrella_4 += data.get('estrella_4', 0)
        estrella.estrella_5 += data.get('estrella_5', 0)
        estrella.save()

        serializer = EstrellaDetailSerializer(estrella)
        return Response({'message': 'estrellas actualizadas con éxito.', 'data': serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, id, format=None):
        estrella = get_object_or_404(Estrellas, id=id)
        estrella.delete()
        return Response({'message': 'Datos eliminados con  exito'}, status=status.HTTP_204_NO_CONTENT)

class AgenciasLimaAPIView(APIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)


    def get(self, request, id=None, format=None):
        if id:
            agencia_lima = get_object_or_404(AgenciasLima, id=id)
            serializer = AgenciaslimaDetailSerializer(agencia_lima)
            empresa = agencia_lima.empresa
            distritos = agencia_lima.distritos.all()
            
            return Response({
            'Agencias_lima': serializer.data,
            'Empresa': EmpresaDetailSerializer(empresa).data,
            'Distritos': DistritosDetailSerializer(distritos, many=True).data
        })
        else:
            agencias_Lima = AgenciasLima.objects.all()
            serializer = AgenciasLimaSerializers(agencias_Lima, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AgenciasLimaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos creados con éxito', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None, format=None):
        agencia_lima = get_object_or_404(AgenciasLima, id=id)
        serializer = AgenciasLimaSerializers(agencia_lima, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos actualizados con éxito', 'data': serializer.data}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        agencia_lima = get_object_or_404(AgenciasLima, id=id)
        agencia_lima.delete()
        return Response({'message': 'Datos eliminados con éxito'}, status=status.HTTP_204_NO_CONTENT)

class LoginAPIView(APIView):
    def post(self, request, format=None):
        email = request.data.get('email')
        password = request.data.get('contrasenia')

        user = get_object_or_404(Usuarios, email=email)

        if user.contrasenia == password:
            return Response({
                'message': 'Inicio de sesión exitoso',
                'id': user.id,
                'nombre': user.nombre
            }, status=status.HTTP_200_OK)
        else:
            return  Response({'detail': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)


class UsuariosAPIView(APIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)
        
    def get(self, request, id=None, format=None):
        if id:
            usuario = get_object_or_404(Usuarios, id=id)
            serializer = UsuarioDetailSerializer(usuario)
            comentarios = Comentarios.objects.filter(usuario=usuario)
            return Response({
                'Usuario': serializer.data,
                'Comentarios': ComentariosDetailSerializer(comentarios, many=True).data
            })
        else:
            usuarios = Usuarios.objects.all()
            serializer = UsuarioSerializers(usuarios, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        email = request.data.get('email')
        if Usuarios.objects.filter(email=email).exists():
            return Response({'detail': 'Ya existe un usuario con ese correo electrónico'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = UsuarioSerializers(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.contrasenia = request.data.get('contrasenia')  # Almacena la contraseña en texto plano
            user.save()
            return Response({'message': 'Usuario creado con éxito', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None, format=None):
        usuario = get_object_or_404(Usuarios, id=id)
        data = request.data
        email = data.get('email')
        if Usuarios.objects.filter(email=email).exclude(id=id).exists():
            return Response({'Ya existe un usuario con este coreo electrinico'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UsuarioSerializers(usuario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos actualizados con exito', 'data': serializer.data}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        usuario = get_object_or_404(Usuarios, id=id)
        usuario.delete()
        return Response({'message': 'Usuario eliminado con exito'}, status=status.HTTP_204_NO_CONTENT)


class ComentariosAPIView(APIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def get(self, request, id=None, format=None):
        if id:
            comentario = get_object_or_404(Comentarios, id=id)
            serializer = ComentariosSerializers(comentario)
        else:
            comentarios = Comentarios.objects.all()
            serializer = ComentariosSerializers(comentarios, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ComentariosSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Comentario creado con exito', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None, format=None):
        comentario = get_object_or_404(Comentarios, id=id)
        serializer = ComentariosSerializers(comentario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos actualizados con exito', 'data': serializer.data}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        comentario = get_object_or_404(Comentarios, id=id)
        comentario.delete()
        return Response({'message': 'Comentario eliminado con éxito'}, status=status.HTTP_204_NO_CONTENT)

class DepartamentosAPIView(APIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def get(self, request, id=None, format=None):
        if id:
            departamento = get_object_or_404(Departamentos, id=id)
            serializer = DepartamentosSerializers(departamento)
            provincias = Provincias.objects.filter(departamento=departamento)
            return Response({
                'Departamento': serializer.data,
                'Provincias': ProvinciasDetailSerializer(provincias, many=True).data
            })
        else:
            departamentos = Departamentos.objects.all()
            serializer = DepartamentosSerializers(departamentos, many=True)
        return Response(serializer.data)



class ProvinciasAPIView(APIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def get(self, request, id=None, format=None):
        if id:
            provincia = get_object_or_404(Provincias, id=id)
            serializer = ProvinciasSerializers(provincia)
            distritos = Distritos.objects.filter(provincia=provincia)
            departamento = provincia.departamento
            return Response({
                'Provincia': serializer.data,
                'Distritos': DistritosDetailSerializer(distritos, many=True).data,
                'Departamento': DepartamentosSerializers(departamento).data
            })
        else:
            provincias = Provincias.objects.all()
            serializer = ProvinciasSerializers(provincias, many=True)
        return Response(serializer.data)



class DistritosAPIView(APIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def get(self, request, id=None, format=None):
        if id:
            distrito = get_object_or_404(Distritos, id=id)
            serializer = DistritosSerializers(distrito)
            provincia = Provincias.objects.filter(distrito=distrito)
            return Response({
                'Distrito': serializer.data,
                'Provincia': ProvinciasSerializers(provincia, many=True).data
            })
        else:
            distritos = Distritos.objects.all()
            serializer = DistritosSerializers(distritos, many=True)
        return Response(serializer.data)

class DistritosagenciasAPIView(APIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def get(self, request, id=None, format=None):
        if id:
            distrito = get_object_or_404(Distritos, id=id)
            serializer = DistritosDetailSerializer(distrito)
            agencias = AgenciasLima.objects.filter(distritos=distrito)
            return Response({
                'Distrito': serializer.data,
                'Agencias': AgenciaslimaDetailSerializer(agencias, many=True).data
            })
        else:
            return Response({'detail': 'ID de distrito no proporcionado.'}, status=status.HTTP_400_BAD_REQUEST)
