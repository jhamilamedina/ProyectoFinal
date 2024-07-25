from django.urls import path
from rest_framework import routers
from .api import EmpresaAPIView

urlpatterns = [
    # Endpoint para listar y crear Empresas
    path('api/empresas/', EmpresaAPIView.as_view(), name='empresas-list-create'),
    # Endpoint para obtener, actualizar y eliminar una Empresa
    path('api/empresas/<int:id>/', EmpresaAPIView.as_view(), name='empresas-detail-update-delete'),
]