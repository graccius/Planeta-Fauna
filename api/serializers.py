from django.shortcuts import render
from rest_framework import serializers
from animais.models import Reino, Filo, Classe, Ordem, Familia, Genero, Especie
from .models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user


class ReinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reino
        fields = ['id', 'nome', 'descricao', 'imagem']

class FiloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filo
        fields = ['id', 'nome', 'descricao', 'imagem', 'reino']

class ClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = ['id', 'nome', 'descricao', 'imagem', 'filo']

class OrdemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordem
        fields = ['id', 'nome', 'descricao', 'imagem', 'classe']

class FamiliaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familia
        fields = ['id', 'nome', 'descricao', 'imagem', 'ordem']

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ['id', 'nome', 'descricao', 'imagem', 'familia']

class EspecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especie
        fields = ['id', 'nome', 'descricao', 'imagem', 'genero']
        
        

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        password = validated_data.get('password')
        if password:
            instance.set_password(password)

        instance.save()
        return instance
