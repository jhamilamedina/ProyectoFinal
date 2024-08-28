from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from .models import Departamentos, Provincias
from .serializers import DepartamentosSerializer, ProvinciasDetailSerializer, EmpresaDetailSerializer

class DepartamentosAPIView(APIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def get(self, request, id=None, format=None):
        if id:
            departamento = get_object_or_404(Departamentos, id=id)
            serializer = DepartamentosSerializer(departamento)
            provincias = Provincias.objects.filter(departamento=departamento)
            return Response({
                'departamento': serializer.data,
                'provincias': ProvinciasDetailSerializer(provincias, many=True).data
            })
        else:
            departamentos = Departamentos.objects.all()
            serializer = DepartamentosSerializer(departamentos, many=True)
            return Response(serializer.data)

class EmpresaDetailView(generics.RetrieveAPIView):
    queryset = Empresas.objects.all()
    serializer_class = EmpresaDetailSerializer