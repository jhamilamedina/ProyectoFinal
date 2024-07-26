from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from .models import Empresa, Usuario, AgenciaLima,Comentario
from .serializers import EmpresaSerializer, UsuarioSerializers, AgenciasLimaSerializers, ComentariosSerializers

message1 = 'No existe'
message2 = 'No registrado en la base de datos'
message3 = 'No se puede eliminar porque no existe'


class EmpresaAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_object(self, id):
        try:
            return Empresa.objects.get(id=id)
        except Empresa.DoesNotExist:
            return None

    def get(self, request, id=None, format=None):
        if id:
            empresa = self.get_object(id)
            if empresa is None:
                return Response({'message': message1}, status=status.HTTP_404_NOT_FOUND)
            serializer = EmpresaSerializer(empresa)
        else:
            empresas = Empresa.objects.all()
            serializer = EmpresaSerializer(empresas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmpresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Empresa creada con exito', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id=None, format=None):
        empresa = self.get_object(id)
        if empresa is None:
            return Response({'message': message2}, status=status.HTTP_404_NOT_FOUND)
        serializer = EmpresaSerializer(empresa, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos actualizados con exito', 'data': serializer.data}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        empresa = self.get_object(id)
        if empresa is None:
            return Response({'message': message3}, status=status.HTTP_404_NOT_FOUND)
        empresa.delete()
        return Response({'message': 'Empresa eliminada con  exito'}, status=status.HTTP_204_NO_CONTENT)


class AgenciasLimaAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_object(self, id):
        try:
            return AgenciaLima.objects.get(id=id)
        except AgenciaLima.DoesNotExist:
            return None

    def get(self, request, id=None, format=None):
        if id:
            agencia_lima = self.get_object(id)
            if agencia_lima is None:
                return Response({'message': message1}, status=status.HTTP_404_NOT_FOUND)
            serializer = AgenciasLimaSerializers(agencia_lima)
        else:
            agencias_Lima = AgenciaLima.objects.all()
            serializer = AgenciasLimaSerializers(agencias_Lima, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AgenciasLimaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Agencia creada con exito', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None, format= None):
        agencia_lima = self.get_object(id)
        if agencia_lima is None:
            return Response({'message': message2},status=status.HTTP_404_NOT_FOUND)
        serializer = AgenciasLimaSerializers(agencia_lima, data=request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos actualizados con exito', 'data':serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        agencia_lima = self.get_object(id)
        if agencia_lima is None:
            return Response({'message': message3}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        agencia_lima.delete()
        return Response({'message': 'Agencia eliminada con exito'}, status=status.HTTP_204_NO_CONTENT)


class UsuarioAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_object(self, id):
        try:
            return Usuario.objects.get(id=id)
        except Usuario.DoesNotExist:
            return None
        
    def get(self, request, id=None, format=None):
        if id:
            usuario = self.get_object(id)
            if usuario is None:
                return Response({'message': message1}, status=status.HTTP_404_NOT_FOUND)
            serializer = UsuarioSerializers(usuario)
        else:
            usuarios = Usuario.objects.all()
            serializer = UsuarioSerializers(usuarios, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = UsuarioSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Usuario creado con exito', 'data':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None, format=None):
        usuario = self.get_object(id)
        if usuario is None:
            return Response({'message': message2}, status=status.HTTP_404_NOT_FOUND)
        serializer = UsuarioSerializers(usuario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos actualizados con exito', 'data': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        usuario = self.get_object(id)
        if usuario is None:
            return Response({'message': message3}, status=status.HTTP_404_NOT_FOUND)
        usuario.delete()
        return Response({'message': 'Usuario eliminado con exito'}, status=status.HTTP_204_NO_CONTENT)


class ComentariosAPIViews(APIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_object(self, id):
        try:
            return Comentario.objects.get(id=id)
        except Comentario.DoesNotExist:
            return None

    def get(self, request, id=None, format=None):
        if id:
            comentario = self.get_object(id)
            if comentario is None:
                return Response({'message': message1}, status=status.HTTP_404_NOT_FOUND)
            serializer = ComentariosSerializers(comentario)
        else:
            comentarios = Comentario.objects.all()
            serializer = ComentariosSerializers(comentarios, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ComentariosSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Comentario creado con exito', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None, format=None):
        comentario = self.get_object(id)
        if comentario is None:
            return Response({'message': message2}, status=status.HTTP_404_NOT_FOUND)
        serializer = ComentariosSerializers(comentario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos actualizados con exito', 'data': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        comentario = self.get_object(id)
        if comentario is None:
            return Response({'message': message3}, status=status.HTTP_404_NOT_FOUND)
        comentario.delete()
        return Response({'message': 'Comentario eliminado con exito'}, status=status.HTTP_204_NO_CONTENT)