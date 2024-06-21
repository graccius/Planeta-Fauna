from rest_framework import viewsets, generics
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from animais.models import Reino, Filo, Classe, Ordem, Familia, Genero, Especie  # Importe o modelo de usuário personalizado
from .models import CustomUser
from rest_framework.permissions import AllowAny
from .serializers import (
    ReinoSerializer, FiloSerializer, ClasseSerializer, OrdemSerializer, 
    FamiliaSerializer, GeneroSerializer, EspecieSerializer, RegisterSerializer, CustomUserSerializer
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    # Permissões para permitir que somente usuários autenticados e administradores acessem essas views
    permission_classes = [IsAuthenticated, IsAdminUser]

## CRUD ##
class ReinoViewSet(viewsets.ModelViewSet):
    queryset = Reino.objects.all()
    serializer_class = ReinoSerializer

class FiloViewSet(viewsets.ModelViewSet):
    queryset = Filo.objects.all()
    serializer_class = FiloSerializer

class ClasseViewSet(viewsets.ModelViewSet):
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer

class OrdemViewSet(viewsets.ModelViewSet):
    queryset = Ordem.objects.all()
    serializer_class = OrdemSerializer

class FamiliaViewSet(viewsets.ModelViewSet):
    queryset = Familia.objects.all()
    serializer_class = FamiliaSerializer

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class EspecieViewSet(viewsets.ModelViewSet):
    queryset = Especie.objects.all()
    serializer_class = EspecieSerializer

class DetalhesEspeciesViewSet(viewsets.ModelViewSet):
    queryset = Especie.objects.all()
    serializer_class = EspecieSerializer

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        login(self.request, user)
