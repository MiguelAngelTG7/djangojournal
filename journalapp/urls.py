from django.urls import path
from .views import PosteosApiView, UnPosteoApiView, RegistroUsuarioApiView, PerfilUsuarioApiView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('posteos', PosteosApiView.as_view()),
    path('posteos/<int:id>', UnPosteoApiView.as_view()),
    path('registro', RegistroUsuarioApiView.as_view()),
    path('login', TokenObtainPairView.as_view()),
    path('perfil', PerfilUsuarioApiView.as_view())
]