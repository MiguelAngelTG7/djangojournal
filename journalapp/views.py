from rest_framework import generics, response, status, request, permissions
from .models import PosteosModel, UsuarioModel
from .serializers import PosteosSerializer, RegistroUsuarioSerializer, MostrarUsuarioSerializer
from .permissions import SoloUsuario

class PosteosApiView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, SoloUsuario] 
    queryset = PosteosModel.objects.all()
    serializer_class = PosteosSerializer

class UnPosteoApiView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, SoloUsuario] 
    def get(self, request, id):
        resultado = PosteosModel.objects.filter(id=id).first()
        if resultado is None:
            return response.Response(data={
                'message' : 'El Posteo no existe'
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializador = PosteosSerializer(instance=resultado)
                
        return response.Response(data={
            'message' : serializador.data                 
        }, status=status.HTTP_200_OK)
    
    def put(self, request: request.Request, id):
        resultado = PosteosModel.objects.filter(id=id).first()
        if resultado is None:
            return response.Response(data={
                'message' : 'El Posteo no existe'
            }, status=status.HTTP_404_NOT_FOUND)
        
        data_serializada = PosteosSerializer(data= request.data)
        if data_serializada.is_valid():
            resultado.title = data_serializada.data.get('title')
            resultado.body = data_serializada.data.get('body')
            resultado.save()
            return response.Response(data={
                'message' : 'Posteo Actualizado Exitosamente'
            })

        else:
            return response.Response(data={
                'message' : 'Error al Actualizar la Categoria',
                'content' : data_serializada.errors
            })
    
    def delete(self, request, id):
        resultado = PosteosModel.objects.filter(id=id).first()
        if resultado is None:
            return response.Response(data={
                'message': 'El Posteo no Existe'
            }, status=status.HTTP_404_NOT_FOUND)

        resultado.delete()
        return response.Response(data={
            'message': 'Posteo Eliminado Exitosamente'
        }, status=status.HTTP_200_OK)

class RegistroUsuarioApiView(generics.CreateAPIView):
    def post(self, request: request.Request):
        serializador = RegistroUsuarioSerializer(data = request.data)
        if serializador.is_valid():
            nuevo_usuario = UsuarioModel(**serializador.validated_data)
            nuevo_usuario.set_password(serializador.validated_data.get('password'))

            nuevo_usuario.save()
            return response.Response(data={
                'message' : 'Usuario Creado Exitosamente'
            }, status=status.HTTP_201_CREATED)

        else:
            return response.Response(data={
                'message' : 'Error al Registrar al usuario',
                'content' : serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    
class PerfilUsuarioApiView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request: request.Request):
        usuario_encontrado = MostrarUsuarioSerializer(instance = request.user)
        return response.Response(data={
            'content' : usuario_encontrado.data
        })