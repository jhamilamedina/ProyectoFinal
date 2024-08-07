from django.contrib.auth.backends import BaseBackend
from API_ENVIA_YA.models import Usuarios

class CustomBackend(BaseBackend):
    def authenticate(self, request, email=None, contrasenia=None, **kwargs):
        try:
            usuario = Usuarios.objects.get(email=email)
            if usuario.contrasenia == contrasenia:
                return usuario
        except Usuarios.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Usuarios.objects.get(pk=user_id)
        except Usuarios.DoesNotExist:
            return None
