from rest_framework.test import APITestCase
from financas.models import Receita
from rest_framework import status
from django.urls import reverse
from datetime import datetime


class ReceitasTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Receitas-list')
        self.receita = Receita.objects.create(
            descricao_receita='Salario', valor_receita=1500, data_receita=datetime(2022, 8, 19)
        )

    def test_get_receitas(self):
        """Teste requisição GET para visulaizar todas receitas"""
        response = self.client.get('/receitas/')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_post_receita(self):
        """Teste requisição POST de uma receita"""
        data = {
            'descricao_receita': 'Salario Teste',
            'valor_receita': '1500',
            'data_receita': '2022-08-19'
        }

        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_delete_receita(self):
        """Teste de requisição DELETE em uma receita"""
        response = self.client.delete('/receitas/1/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_put_receita(self):
        """Teste requisição PUT para atualizar uma receita"""
        data = {
            'descricao_receita': 'Decimo Terceiro',
            'valor_receita': '1500',
            'data_receita': '2022-08-19'
        }
        response = self.client.put(f'/receitas/{self.receita.id}/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_post_campos_imcompletos(self):
        """Teste de requisição POST com campos incompletos"""
        data = {
            'descricao_receita': 'Teste',
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_busca_por_descricao(self):
        """Teste requisição GET para buscar receita por descricao"""
        response = self.client.get('/receitas/?descricao_receita=teste/')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_get_filtro_mensal(self):
        response = self.client.get('/receitas/2022/08/')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
