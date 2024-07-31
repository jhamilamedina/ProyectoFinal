from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from .models import Empresa, Valoracion, Estrella,Usuario, AgenciaLima, Comentario, Departamento, Provincia, Distrito
from .serializers import EmpresaSerializer, ValoracionSerializers, EstrellasSerializers, UsuarioSerializers, AgenciasLimaSerializers, ComentariosSerializers, DepartamentosSerializers, ProvinciasSerializers, DistritosSerializers
from .serializers import EmpresaDetailSerializer, AgenciaslimaDetailSerializer, DistritosDetailSerializer, ValoracionDetailSerializer, EstrellaDetailSerializer, ComentariosDetailSerializer, UsuarioDetailSerializer, ProvinciasDetailSerializer


class EmpresasAPIView(APIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def get(self, request, id=None, format=None):
        if id:
            empresa = get_object_or_404(Empresa,id=id)
            serializer = EmpresaDetailSerializer(empresa)
            valoraciones = Valoracion.objects.filter(empresa=empresa)
            estrellas = Estrella.objects.filter(empresa=empresa)
            comentarios = Comentario.objects.filter(empresa=empresa)
            agenciaslima = AgenciaLima.objects.filter(empresa=empresa)
            return Response({
                'empresa': serializer.data,
                'Sus agencias': AgenciaslimaDetailSerializer(agenciaslima, many=True).data,
                'Sus valoraciones': ValoracionDetailSerializer(valoraciones, many=True).data,
                'Sus estrellas': EstrellaDetailSerializer(estrellas, many=True).data,
                'Sus comentarios': ComentariosDetailSerializer(comentarios, many=True).data
            })
        else:
            empresas = Empresa.objects.all()
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
        empresa = get_object_or_404(Empresa, id=id)
        serializer = EmpresaSerializer(empresa, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos actualizados con exito', 'data': serializer.data, 'id': id}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        empresa = get_object_or_404(Empresa, id=id)
        empresa.delete()
        return Response({'message': 'Datos eliminados con  exito', 'id': id}, status=status.HTTP_204_NO_CONTENT)

class ValoracionesAPIView(APIView):
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

class EstrellasAPIView(APIView):
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
            serializer = AgenciaslimaDetailSerializer(agencia_lima)
            empresa = agencia_lima.empresa
            distritos = agencia_lima.distrito
            
            return Response({
            'agencias_lima': serializer.data,
            'empresa': EmpresaDetailSerializer(empresa).data,
            'distritos': DistritosDetailSerializer(distritos).data
        })
        else:
            agencias_Lima = AgenciaLima.objects.all()
            serializer = AgenciasLimaSerializers(agencias_Lima, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AgenciasLimaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos creados con éxito', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None, format=None):
        agencia_lima = get_object_or_404(AgenciaLima, id=id)
        serializer = AgenciasLimaSerializers(agencia_lima, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos actualizados con éxito', 'data': serializer.data}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        agencia_lima = get_object_or_404(AgenciaLima, id=id)
        agencia_lima.delete()
        return Response({'message': 'Datos eliminados con éxito'}, status=status.HTTP_204_NO_CONTENT)



class UsuariosAPIView(APIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)
        
    def get(self, request, id=None, format=None):
        if id:
            usuario = get_object_or_404(Usuario, id=id)
            serializer = UsuarioDetailSerializer(usuario)
            comentarios = Comentario.objects.filter(usuario=usuario)
            return Response({
                'usuario': serializer.data,
                'Sus comentarios': ComentariosDetailSerializer(comentarios, many=True).data
            })
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


class ComentariosAPIView(APIView):
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
        return Response({'message': 'Comentario eliminado con éxito'}, status=status.HTTP_204_NO_CONTENT)

class DepartamentosAPIView(APIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def get(self, request, id=None, format=None):
        if id:
            departamento = get_object_or_404(Departamento, id=id)
            serializer = DepartamentosSerializers(departamento)
            provincias = Provincia.objects.filter(departamento=departamento)
            return Response({
                'departamento': serializer.data,
                'provincias': ProvinciasDetailSerializer(provincias, many=True).data
            })
        else:
            departamentos = Departamento.objects.all()
            serializer = DepartamentosSerializers(departamentos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DepartamentosSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos creados con éxito', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, id=None, format=None):
        departamento = get_object_or_404(Departamento, id=id)
        serializer = DepartamentosSerializers(departamento, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos actualizados con exito', 'data': serializer.data}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProvinciasAPIView(APIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def get(self, request, id=None, format=None):
        if id:
            provincia = get_object_or_404(Provincia, id=id)
            serializer = ProvinciasSerializers(provincia)
            distritos = Distrito.objects.filter(provincia=provincia)
            return Response({
                'provincia': serializer.data,
                'distrito': DistritosDetailSerializer(distritos, many=True).data
            })
        else:
            provincias = Provincia.objects.all()
            serializer = ProvinciasSerializers(provincias, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProvinciasSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos creados con exito', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None, format=None):
        provincia = get_object_or_404(Provincia, id=id)
        serializer = ProvinciasSerializers(provincia, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Datos actualizados con exito', 'data': serializer.data}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DistritosAPIView(APIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def get(self, request, id=None, format=None):
        if id:
            distrito = get_object_or_404(Distrito, id=id)
            serializer = DistritosSerializers(distrito)
            provincia = Provincia.objects.filter(distrito=distrito)
            return Response({
                'distrito': serializer.data,
                'provincia': ProvinciasSerializers(provincia, many=True).data
            })
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
