from rest_framework import serializers
from .models import PosteosModel, UsuarioModel

class PosteosSerializer(serializers.ModelSerializer):
    class Meta:
        model = PosteosModel
        fields = '__all__'

class RegistroUsuarioSerializer(serializers.ModelSerializer):
    class Meta: 
        model = UsuarioModel
        fields = '__all__'

class MostrarUsuarioSerializer(serializers.ModelSerializer):
    class Meta: 
        model = UsuarioModel
        exclude = ['password','is_staff','user_permissions', 'groups','last_login','is_superuser']