from django.urls import path
from rest_framework import routers
from .api import EmpresaAPIView, UsuarioAPIView

urlpatterns = [
    # Endpoint para listar y crear Empresas
    path('api/empresas/', EmpresaAPIView.as_view(), name='empresas-list-create'),
    # Endpoint para obtener, actualizar y eliminar una Empresa
    path('api/empresas/<int:id>/', EmpresaAPIView.as_view(), name='empresas-detail-update-delete'),
    # Endpoint para listar y crear usuarios
    path('api/usuarios/', UsuarioAPIView.as_view(), name='usuarios-list-create'),
    # Endpoint para obtener, actualizar y eliminar un usuario
    path('api/usuarios/<int:id>/', UsuarioAPIView.as_view(), name='usuarios-detail-update-delete'),
]