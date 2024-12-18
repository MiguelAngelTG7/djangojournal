from django.contrib.auth.models import BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_superuser(self, correo, nombre, apellido, password):
        if not correo:
            raise ValueError('El Usuario debe tener un correo')
        
        correo_normalizado = self.normalize_email(correo)
        nuevo_usuario = self.model(correo=correo_normalizado, nombre=nombre, apellido=apellido)
        nuevo_usuario.set_password(password)

        nuevo_usuario.is_superuser = True
        nuevo_usuario.is_staff = True
        nuevo_usuario.save()
