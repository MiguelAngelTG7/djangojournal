from rest_framework.permissions import BasePermission

class SoloUsuario(BasePermission):
    message = 'Solo los usuarios pueden acceder a estas rutas'
    def has_permission(self, request, view):
        tipoUsuario = request.user.tipoUsuario
        if tipoUsuario == 'USER':
            return True
        else:
            return False