from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import Empresas, Valoraciones, Estrellas,Usuarios, AgenciasLima, Comentarios, Departamentos, Provincias, Distritos
from .serializers import EmpresaSerializer, ValoracionSerializers, EstrellasSerializers, UsuarioSerializers, AgenciasLimaSerializers, ComentariosSerializers, DepartamentosSerializers, ProvinciasSerializers, DistritosSerializers
from .serializers import EmpresaDetailSerializer, AgenciaslimaDetailSerializer, DistritosDetailSerializer, ValoracionDetailSerializer, EstrellaDetailSerializer, ComentariosDetailSerializer, UsuarioDetailSerializer, ProvinciasDetailSerializer


class EmpresasAPIView(APIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def get(self, request, id=None, format=None):
        # Método GET para obtener los datos de una o varias empresas.
        if id:
            # Si se proporciona un ID, obtenemos los detalles de una empresa específica.
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
            # Si no se proporciona un ID, obtenemos todas las empresas.
            empresas = Empresas.objects.all()
            serializer = EmpresaSerializer(empresas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # Método POST para crear una nueva empresa.
        serializer = EmpresaSerializer(data=request.data)
        if serializer.is_valid():
            empresa = serializer.save()
            mensaje = f'Datos creados con exito, con ID: {empresa.id}'
            return Response({'message': mensaje,'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id=None, format=None):
        # Método POST para crear una nueva empresa.
        empresa = get_object_or_404(Empresas, id=id)
        serializer = EmpresaSerializer(empresa, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos actualizados con exito', 'data': serializer.data, 'id': id}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        # Método DELETE para eliminar una empresa por su ID.
        empresa = get_object_or_404(Empresas, id=id)
        empresa.delete()
        return Response({'message': 'Datos eliminados con  exito', 'id': id}, status=status.HTTP_204_NO_CONTENT)

class ValoracionesAPIView(APIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def get(self, request, id=None, format=None):
        if id:
            valoracion = get_object_or_404(Valoraciones,id=id)
            serializer = ValoracionSerializers(valoracion)
        else:
            valoraciones = Valoraciones.objects.all()
            serializer = ValoracionSerializers(valoraciones, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # Método POST para crear una nueva valoración.
        empresa_id = request.data.get('empresa')
        try:
            empresa = Empresas.objects.get(id=empresa_id)
        except Empresas.DoesNotExist:
            return Response({'detail': 'Empresa no encontrada.'}, status=status.HTTP_404_NOT_FOUND)
        
        if Valoraciones.objects.filter(empresa=empresa).exists():
            return Response({'detail': 'Ya existe una valoración para esta empresa.'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = ValoracionSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Valoración creada con éxito.', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id=None, format=None):
        # Método POST para crear una nueva valoración.
        try:
            valoracion = Valoraciones.objects.get(id=id)
        except Valoraciones.DoesNotExist:
            return Response({'detail': 'Valoración no encontrada.'}, status=status.HTTP_404_NOT_FOUND)
        
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

        serializer = ValoracionDetailSerializer(valoracion)
        return Response({'message': 'Valoración actualizada con éxito.', 'data': serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, id, format=None):
        # Método DELETE para eliminar una valoración por su ID.
        valoracion = get_object_or_404(Valoraciones, id=id)
        valoracion.delete()
        return Response({'message': 'Datos eliminados con  exito'}, status=status.HTTP_204_NO_CONTENT)

class EstrellasAPIView(APIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def get(self, request, id=None, format=None):
        # Método GET para obtener los datos de una o varias calificaciones de estrellas.
        if id:
            estrella = get_object_or_404(Estrellas, id=id)
            serializer = EstrellasSerializers(estrella)
        else:
            estrellas = Estrellas.objects.all()
            serializer = EstrellasSerializers(estrellas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # Método POST para crear una nueva calificación de estrellas.
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
        # Método PUT para actualizar una calificación de estrellas existente.
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
        # Método DELETE para eliminar una calificación de estrellas por su ID.
        estrella = get_object_or_404(Estrellas, id=id)
        estrella.delete()
        return Response({'message': 'Datos eliminados con  exito'}, status=status.HTTP_204_NO_CONTENT)

class AgenciasLimaAPIView(APIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)


    def get(self, request, id=None, format=None):
        # Método GET para obtener los datos de una o varias agenciasLima.
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
        # Método POST para crear una nueva agenciaLima.
        serializer = AgenciasLimaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos creados con éxito', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None, format=None):
        # Método PUT para actualizar los datos de una agenciaLima.
        agencia_lima = get_object_or_404(AgenciasLima, id=id)
        serializer = AgenciasLimaSerializers(agencia_lima, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos actualizados con éxito', 'data': serializer.data}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        # Método DELETE para eliminar una agenciaLima por su ID.
        agencia_lima = get_object_or_404(AgenciasLima, id=id)
        agencia_lima.delete()
        return Response({'message': 'Datos eliminados con éxito'}, status=status.HTTP_204_NO_CONTENT)

class LoginAPIView(APIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def post(self, request, format=None):
        # Extraemos el email y la contraseña del cuerpo de la solicitud
        email = request.data.get('email')
        contrasenia = request.data.get('contrasenia')

        # Intentamos autenticar al usuario utilizando el email como nombre de usuario
        # y la contraseña proporcionada. El método `authenticate` busca un usuario
        # con estas credenciales y devuelve un objeto de usuario si tiene éxito.
        user = authenticate(request, email=email, contrasenia=contrasenia)

        if user is not None:
            # Si la autenticación es exitosa, retornamos un mensaje de éxito y
            # algunos detalles del usuario (en este caso, el nombre).
            return Response({
                'message': 'Inicio de sesión exitoso',
                'Nombre': user.nombre
            }, status=status.HTTP_200_OK)
        else:
            # Si la autenticación falla, devolvemos una respuesta con un mensaje de error
            # y un código de estado 401 indicando que las credenciales son inválidas.
            return Response({'detail': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)


class UsuariosAPIView(APIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)
        
    def get(self, request, id=None, format=None):
        # Método GET para obtener los datos de uno o varios usuarios.
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
        # Método POST para crear un nuevo usuario.
        email = request.data.get('email')
        if Usuarios.objects.filter(email=email).exists():
            return Response({'Ya existe un usuario con ese correo electronico'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UsuarioSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Usuario creado con exito', 'data':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None, format=None):
        # Método PUT para actualizar los datos de un usuario.
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
        # Método DELETE para eliminar un usuario por su ID.
        usuario = get_object_or_404(Usuarios, id=id)
        usuario.delete()
        return Response({'message': 'Usuario eliminado con exito'}, status=status.HTTP_204_NO_CONTENT)


class ComentariosAPIView(APIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def get(self, request, id=None, format=None):
        # Método GET para obtener los datos de uno o varios comentarios.
        if id:
            comentario = get_object_or_404(Comentarios, id=id)
            serializer = ComentariosSerializers(comentario)
        else:
            comentarios = Comentarios.objects.all()
            serializer = ComentariosSerializers(comentarios, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # Método POST para crear un nuevo comentario.
        serializer = ComentariosSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Comentario creado con exito', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None, format=None):
        # Método PUT para actualizar un comentario existente.
        comentario = get_object_or_404(Comentarios, id=id)
        serializer = ComentariosSerializers(comentario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos actualizados con exito', 'data': serializer.data}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        # Método DELETE para eliminar un comentario por su ID.
        comentario = get_object_or_404(Comentarios, id=id)
        comentario.delete()
        return Response({'message': 'Comentario eliminado con éxito'}, status=status.HTTP_204_NO_CONTENT)

class DepartamentosAPIView(APIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def get(self, request, id=None, format=None):
        # Método GET para obtener los datos de uno o varios Departamentos.
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
        # Método GET para obtener los datos de uno o varias Provincias.
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
        # Método GET para obtener los datos de uno o varios Distritos.
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
        # Método GET para obtener los datos de uno o varias agenciasLima segun el ID de un Distrito.
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



