import json
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from animais.models import Reino, Filo, Classe, Ordem, Familia, Genero, Especie

class ReinoListCreateAPIViewTest(APITestCase):
    def setUp(self):
        # Dados para criar os Reinos sem imagem
        dados_reinos = [
            {'nome': 'Animalia', 'descricao': 'Reino Animal'},
            {'nome': 'Plantae', 'descricao': 'Reino Plantae'},
            {'nome': 'Monera', 'descricao': 'Reino Monera'},
            {'nome': 'Fungi', 'descricao': 'Reino Fungi'},
            {'nome': 'Protista', 'descricao': 'Reino Protista'}
        ]
        
        # Criando os Reinos e armazenando os IDs
        self.ids_reinos = []
        for dados_reino in dados_reinos:
            response = self.client.post('/api/reinos/', dados_reino)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.ids_reinos.append(response.data['id'])

    def test_criar_reino(self):
        # Verificar se os reinos foram criados no setUp
        self.assertEqual(len(self.ids_reinos), 5)

    def test_listar_reinos(self):
        # Listando os Reinos criados
        url = reverse('reino-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

        # Imprimindo os nomes, IDs e descrições dos Reinos
        for reino in response.data:
            print(f"ID: {reino['id']}, Nome: {reino['nome']}, Descrição: {reino['descricao']}")

# Repita o padrão para outros modelos e views

class FiloListCreateAPIViewTest(APITestCase):
    def setUp(self):
        # Criando alguns filos para usar no teste
        self.reino = Reino.objects.create(nome='Animalia', descricao='Reino Animal')
        self.filo1 = Filo.objects.create(nome='Mammalia', descricao='Mamíferos', reino=self.reino)

    def test_listar_filo(self):
        # Fazendo a requisição GET para listar os filos
        url = reverse('filo-list')
        response = self.client.get(url)

        # Verificando se a requisição foi bem-sucedida e se todos os filos foram listados
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Número total de filos
        self.assertEqual(response.data[0]['nome'], 'Mammalia')
        
        # Acessando os atributos do objeto Filo corretamente usando a notação de ponto
        print(f"\nNome: {self.filo1.nome}, Descrição: {self.filo1.descricao}, Filo Pertence ao Reino: {self.reino.nome}\n")

class ClasseListCreateAPIViewTest(APITestCase):
    # Testes para ClasseListCreateAPIView
    pass

# Repita o padrão para outros modelos e views