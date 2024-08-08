from django.urls import path
from .api import EmpresasAPIView , ValoracionesAPIView, EstrellasAPIView, UsuariosAPIView, AgenciasLimaAPIView, ComentariosAPIView, DepartamentosAPIView, ProvinciasAPIView,DistritosAPIView, LoginAPIView, DistritosagenciasAPIView

urlpatterns = [
    # Endpoint para listar y crear Empresas
    path('api/empresas/', EmpresasAPIView.as_view(), name='empresas-list-create'),
    # Endpoint para obtener, actualizar y eliminar una Empresa
    path('api/empresas/<int:id>/', EmpresasAPIView.as_view(), name='empresas-detail-update-delete'),

    # Endpoint para listar y crear valoraciones
    path('api/valoraciones/', ValoracionesAPIView.as_view(), name='valoraciones-list-create'),
    # Endpoint para obtener, actualizar y eliminar una valoracion
    path('api/valoraciones/<int:id>/', ValoracionesAPIView.as_view(), name='valoraciones-detail-update-delete'),

    # Endpoint para listar y crear datos en la tabla Estrella
    path('api/estrellas/', EstrellasAPIView.as_view(), name='estrella-list-create'),
    # Endpoint para obtener, actualizar y eliminar datos de la  tabla Estrella
    path('api/estrellas/<int:id>/', EstrellasAPIView.as_view(), name='estrella-detail-update-delete'),

    # Endpoint para inicio de session
    path('api/login/', LoginAPIView.as_view(), name='login'), 

    # Endpoint para listar y crear usuarios
    path('api/usuarios/', UsuariosAPIView.as_view(), name='usuarios-list-create'),
    # Endpoint para obtener, actualizar y eliminar un usuario
    path('api/usuarios/<int:id>/', UsuariosAPIView.as_view(), name='usuarios-detail-update-delete'),

    # Endpoint para listar y crear agencias
    path('api/agenciaslima/', AgenciasLimaAPIView.as_view(), name='agenciaslima-list-create'),
    # Endpoint para obtener, actualizar y eliminar una agencia
    path('api/agenciaslima/<int:id>/', AgenciasLimaAPIView.as_view(), name='agenciaslima-detail-update-delete'),

    # Endpoint para listar y crear comentarios
    path('api/comentarios/', ComentariosAPIView.as_view(), name='comentarios-list-create'),
    # Endpoint para obtener, actualizar y eliminar un comenario
    path('api/comentarios/<int:id>/', ComentariosAPIView.as_view(), name='comentarios-detail-update-delete'),

    # Endpoint para listar y crear departamentos
    path('api/departamentos/', DepartamentosAPIView.as_view(), name='departamentos-list-create'),
    # Endpoint para obtener, actualizar y eliminar un departamento
    path('api/departamentos/<int:id>/', DepartamentosAPIView.as_view(), name='departamentos-detail-update-delete'),

    # Endpoint para listar y crear Provincias
    path('api/provincias/', ProvinciasAPIView.as_view(), name='provincias-list-create'),
    # Endpoint para obtener, actualizar y eliminar una Provincia
    path('api/provincias/<int:id>/', ProvinciasAPIView.as_view(), name='provincias-detail-update-delete'),


    # Endpoint para listar y crear distritos
    path('api/distritos/', DistritosAPIView.as_view(), name='distritos-list-create'),
    # Endpoint para obtener, actualizar y eliminar un distrito
    path('api/distritos/<int:id>/', DistritosAPIView.as_view(), name='distritos-detail-update-delete'),

    path('api/agenciasdistritos/', DistritosagenciasAPIView.as_view(), name='agencias-list'),
    # Endpoint para obtener agencias por distrito
    path('api/agenciasdistritos/<int:id>/', DistritosagenciasAPIView.as_view(), name='distritos-agencias'),


]