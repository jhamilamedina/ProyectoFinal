from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from .models import Empresa, Valoracion, Estrella,Usuario, AgenciaLima, Comentario, Departamento, Provincia, Distrito
from .serializers import EmpresaSerializer, ValoracionSerializers, EstrellasSerializers, UsuarioSerializers, AgenciasLimaSerializers, ComentariosSerializers, DepartamentosSerializers, ProvinciasSerializers, DistritosSerializers


class EmpresaAPIView(APIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def get(self, request, id=None, format=None):
        if id:
            empresa = get_object_or_404(Empresa,id=id)
            serializer = EmpresaSerializer(empresa)
        else:
            empresas = Empresa.objects.all()
            serializer = EmpresaSerializer(empresas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmpresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos creados con exito', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id=None, format=None):
        empresa = get_object_or_404(Empresa, id=id)
        serializer = EmpresaSerializer(empresa, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos actualizados con exito', 'data': serializer.data}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        empresa = get_object_or_404(Empresa, id=id)
        empresa.delete()
        return Response({'message': 'Datos eliminados con  exito'}, status=status.HTTP_204_NO_CONTENT)

class ValoracionAPIView(APIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def get(self, request, id=None, format=None):
        if id:
            valoracion = get_object_or_404(Valoracion,id=id)
            serializer = ValoracionSerializers(valoracion)
        else:
            valoraciones = Valoracion.objects.all()
            serializer = ValoracionSerializers(valoraciones, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ValoracionSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos creados con exito', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id=None, format=None):
        valoracion = get_object_or_404(Valoracion, id=id)
        serializer = ValoracionSerializers(valoracion, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos actualizados con exito', 'data': serializer.data}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        valoracion = get_object_or_404(Valoracion, id=id)
        valoracion.delete()
        return Response({'message': 'Datos eliminados con  exito'}, status=status.HTTP_204_NO_CONTENT)

class EstrellaAPIView(APIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def get(self, request, id=None, format=None):
        if id:
            estrella = get_object_or_404(Estrella, id=id)
            serializer = EstrellasSerializers(estrella)
        else:
            estrellas = Estrella.objects.all()
            serializer = EstrellasSerializers(estrellas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EstrellasSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos creados con exito', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id=None, format=None):
        estrella = get_object_or_404(Estrella, id=id)
        serializer = EstrellasSerializers(estrella, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos actualizados con exito', 'data': serializer.data}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        estrella = get_object_or_404(Estrella, id=id)
        estrella.delete()
        return Response({'message': 'Datos eliminados con  exito'}, status=status.HTTP_204_NO_CONTENT)

class AgenciasLimaAPIView(APIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def get(self, request, id=None, format=None):
        if id:
            agencia_lima = get_object_or_404(AgenciaLima, id=id)
            serializer = AgenciasLimaSerializers(agencia_lima)
        else:
            agencias_Lima = AgenciaLima.objects.all()
            serializer = AgenciasLimaSerializers(agencias_Lima, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AgenciasLimaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos creados con exito', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None, format= None):
        agencia_lima = get_object_or_404(AgenciaLima, id=id)
        serializer = AgenciasLimaSerializers(agencia_lima, data=request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos actualizados con exito', 'data':serializer.data}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        agencia_lima = get_object_or_404(AgenciaLima, id=id)
        agencia_lima.delete()
        return Response({'message': 'Datos eliminados con exito'}, status=status.HTTP_204_NO_CONTENT)


class UsuarioAPIView(APIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)
        
    def get(self, request, id=None, format=None):
        if id:
            usuario = get_object_or_404(Usuario, id=id)
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
        usuario = get_object_or_404(Usuario, id=id)
        serializer = UsuarioSerializers(usuario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos actualizados con exito', 'data': serializer.data}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        usuario = get_object_or_404(Usuario, id=id)
        usuario.delete()
        return Response({'message': 'Usuario eliminado con exito'}, status=status.HTTP_204_NO_CONTENT)


class ComentariosAPIViews(APIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def get(self, request, id=None, format=None):
        if id:
            comentario = get_object_or_404(Comentario, id=id)
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
        comentario = get_object_or_404(Comentario, id=id)
        serializer = ComentariosSerializers(comentario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos actualizados con exito', 'data': serializer.data}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        comentario = get_object_or_404(Comentario, id=id)
        comentario.delete()
        return Response({'message': 'Comentario eliminado con exito'}, status=status.HTTP_204_NO_CONTENT)

class DepartamentosAPIViews(APIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def get(self, request, id=None, format=None):
        if id:
            departamento = get_object_or_404(Departamento, id=id)
            serializer = DepartamentosSerializers(departamento)
        else:
            departamentos = Departamento.objects.all()
            serializer = DepartamentosSerializers(departamentos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        departartamento = DepartamentosSerializers(data=request.data)
        if departartamento.is_valid():
            departartamento.save()
            return Response({'message': 'Datos creados con exito', 'data': departartamento.data}, status=status.HTTP_201_CREATED)
        return Response(departartamento.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None, format=None):
        departamento = get_object_or_404(Departamento, id=id)
        serializer = DepartamentosSerializers(departamento, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos actualizados con exito', 'data': serializer.data}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        departamento = get_object_or_404(Departamento, id=id)
        departamento.delete()
        return Response({'message': 'Datos eliminados con exito'}, status=status.HTTP_204_NO_CONTENT)

class ProvinciasAPIViews(APIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def get(self, request, id=None, format=None):
        if id:
            provincia = get_object_or_404(Provincia, id=id)
            serializer = ProvinciasSerializers(provincia)
        else:
            provincias = Provincia.objects.all()
            serializer = ProvinciasSerializers(provincias, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        provincia = ProvinciasSerializers(data=request.data)
        if provincia.is_valid():
            provincia.save()
            return Response({'message': 'Datos creados con exito', 'data': provincia.data}, status=status.HTTP_201_CREATED)
        return Response(provincia.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None, format=None):
        provincia = get_object_or_404(Provincia, id=id)
        serializer = ProvinciasSerializers(provincia, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos actualizados con exito', 'data': serializer.data}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        provincia = get_object_or_404(Provincia, id=id)
        provincia.delete()
        return Response({'message': 'Datos eliminados con exito'}, status=status.HTTP_204_NO_CONTENT)

class DistritosAPIViews(APIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def get(self, request, id=None, format=None):
        if id:
            distrito = get_object_or_404(Distrito, id=id)
            serializer = DistritosSerializers(distrito)
        else:
            distritos = Distrito.objects.all()
            serializer = DistritosSerializers(distritos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DistritosSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos creados con exito', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None, format=None):
        distrito = get_object_or_404(Distrito, id=id)
        serializer = DistritosSerializers(distrito, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos actualizados con exito', 'data': serializer.data}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        distrito = get_object_or_404(Distrito, id=id)
        distrito.delete()
        return Response({'message': 'Datos eliminados con exito'}, status=status.HTTP_204_NO_CONTENT)