from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .auth_manager import UsuarioManager

class UsuarioModel(AbstractBaseUser, PermissionsMixin):

    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100, unique=True, null=False)
    password = models.TextField(null=False)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    tipoUsuario = models.CharField(max_length=100, choices=[('ADMIN','ADMIN'),('USER','USER')], default='USER', db_column='tipo_usuario')
    createdAt = models.DateField(auto_now_add=True, db_column='created_at')

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre','apellido']

    objects = UsuarioManager()

    class Meta:
        db_table = 'usuarios'

class PosteosModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    title = models.CharField(max_length=100, null=False)
    body = models.CharField(max_length=500, null=False)
    createdAt = models.DateTimeField(auto_now_add=True, db_column='created_at')
    updatedAt = models.DateTimeField(auto_now=True, db_column='updated_at')
    user = models.ForeignKey(to=UsuarioModel, null=False, on_delete=models.CASCADE, db_column='user_id')

    class Meta: 
        db_table = 'posteos'
