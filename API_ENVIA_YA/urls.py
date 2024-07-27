from django.urls import path
from .api import EmpresaAPIView , ValoracionAPIView, EstrellaAPIView, UsuarioAPIView, AgenciasLimaAPIView, ComentariosAPIViews, DepartamentosAPIViews, ProvinciasAPIViews,DistritosAPIViews

urlpatterns = [
    # Endpoint para listar y crear Empresas
    path('api/empresas/', EmpresaAPIView.as_view(), name='empresas-list-create'),
    # Endpoint para obtener, actualizar y eliminar una Empresa
    path('api/empresas/<int:id>/', EmpresaAPIView.as_view(), name='empresas-detail-update-delete'),

    # Endpoint para listar y crear valoraciones
    path('api/valoraciones/', ValoracionAPIView.as_view(), name='valoraciones-list-create'),
    # Endpoint para obtener, actualizar y eliminar una valoracion
    path('api/valoraciones/<int:id>/', ValoracionAPIView.as_view(), name='valoraciones-detail-update-delete'),

    # Endpoint para listar y crear datos en la tabla Estrella
    path('api/estrellas/', EstrellaAPIView.as_view(), name='estrella-list-create'),
    # Endpoint para obtener, actualizar y eliminar datos de la  tabla Estrella
    path('api/estrellas/<int:id>/', EstrellaAPIView.as_view(), name='estrella-detail-update-delete'),

    # Endpoint para listar y crear usuarios
    path('api/usuarios/', UsuarioAPIView.as_view(), name='usuarios-list-create'),
    # Endpoint para obtener, actualizar y eliminar un usuario
    path('api/usuarios/<int:id>/', UsuarioAPIView.as_view(), name='usuarios-detail-update-delete'),

    # Endpoint para listar y crear agencias
    path('api/agenciaslima/', AgenciasLimaAPIView.as_view(), name='agenciaslima-list-create'),
    # Endpoint para obtener, actualizar y eliminar una agencia
    path('api/agenciaslima/<int:id>/', AgenciasLimaAPIView.as_view(), name='agenciaslima-detail-update-delete'),

    # Endpoint para listar y crear comentarios
    path('api/comentarios/', ComentariosAPIViews.as_view(), name='comentarios-list-create'),
    # Endpoint para obtener, actualizar y eliminar un comenario
    path('api/comentarios/<int:id>/', ComentariosAPIViews.as_view(), name='comentarios-detail-update-delete'),

    # Endpoint para listar y crear departamentos
    path('api/departamentos/', DepartamentosAPIViews.as_view(), name='departamentos-list-create'),
    # Endpoint para obtener, actualizar y eliminar un departamento
    path('api/departamentos/<int:id>/', DepartamentosAPIViews.as_view(), name='departamentos-detail-update-delete'),

    # Endpoint para listar y crear Provincias
    path('api/provincias/', ProvinciasAPIViews.as_view(), name='provincias-list-create'),
    # Endpoint para obtener, actualizar y eliminar una Provincia
    path('api/provincias/<int:id>/', ProvinciasAPIViews.as_view(), name='provincias-detail-update-delete'),


    # Endpoint para listar y crear distritos
    path('api/distritos/', DistritosAPIViews.as_view(), name='distritos-list-create'),
    # Endpoint para obtener, actualizar y eliminar un distrito
    path('api/distritos/<int:id>/', DistritosAPIViews.as_view(), name='distritos-detail-update-delete'),
]