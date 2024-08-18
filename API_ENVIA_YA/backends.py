class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, contrasenia=None, **kwargs):
        try:
            usuario = Usuarios.objects.get(email=email)
            if usuario and usuario.contrasenia == contrasenia:
                return usuario
        except Usuarios.DoesNotExist:
            return None