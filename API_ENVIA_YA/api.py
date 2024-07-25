from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from .models import Empresa, Usuario
from .serializers import EmpresaSerializer, UsuarioSerializers


class EmpresaAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_object(self, id):
        try:
            return Empresa.objects.get(id=id)
        except Empresa.DoesNotExist:
            raise Http404

    def get(self, request, id=None, format=None):
        if id:
            empresa = self.get_object(id)
            serializer = EmpresaSerializer(empresa)
        else:
            empresas = Empresa.objects.all()
            serializer = EmpresaSerializer(empresas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmpresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Empresa creada con éxito', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id=None, format=None):
        empresa = self.get_object(id)
        serializer = EmpresaSerializer(empresa, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Empresa actualizada con éxito', 'data': serializer.data}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        empresa = self.get_object(id)
        empresa.delete()
        return Response({'message': 'Empresa eliminada con éxito'}, status=status.HTTP_204_NO_CONTENT)

