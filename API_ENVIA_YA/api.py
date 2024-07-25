from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from .models import Empresa, Usuario
from .serializers import EmpresaSerializer, UsuarioSerializers

message1 = 'Does not exist'
message2 = 'Not registered in the database'
message3 = 'It cannot be deleted because it does not exist'


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
            return Response({'message': 'Successfully created company', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id=None, format=None):
        empresa = self.get_object(id)
        if empresa is None:
            return Response({'message': message2}, status=status.HTTP_404_NOT_FOUND)
        serializer = EmpresaSerializer(empresa, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data updated correctly', 'data': serializer.data}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        empresa = self.get_object(id)
        if empresa is None:
            return Response({'message': message3}, status=status.HTTP_404_NOT_FOUND)
        empresa.delete()
        return Response({'message': 'Company successfully eliminated'}, status=status.HTTP_204_NO_CONTENT)

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
            return Response({'message': 'User created successfully', 'data':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None, format=None):
        usuario = self.get_object(id)
        if usuario is None:
            return Response({'message': message2}, status=status.HTTP_404_NOT_FOUND)
        serializer = UsuarioSerializers(usuario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data updated successfully', 'data': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        usuario = self.get_object(id)
        if usuario is None:
            return Response({'message': message3}, status=status.HTTP_404_NOT_FOUND)
        usuario.delete()
        return Response({'message': 'User successfully deleted'}, status=status.HTTP_204_NO_CONTENT)
    