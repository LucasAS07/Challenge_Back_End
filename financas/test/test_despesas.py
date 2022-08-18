from rest_framework.test import APITestCase
from financas.models import Despesa
from rest_framework import status
from django.urls import reverse
from datetime import datetime


class DespesasTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Despesas-list')
        self.despesa = Despesa.objects.create(
            descricao_despesa='Farmacia', valor_despesa=450, data_despesa=datetime(2022, 8, 18), categoria='S'
        )

    def test_get_despesa(self):
        """Teste para visualizar um GET de despesas"""
        response = self.client.get('/despesas/')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_post_em_despesas(self):
        """Teste para realizar um requisiçaõ POST em despesas"""
        data = {
            'descricao_despesa': 'DespesaTeste',
            'valor_despesa': 100,
            'data_despesa': '2022-08-18',
            'categoria': 'A',
        }

        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_delete_despesa(self):
        """Teste para verificar a requisição DELETE em uma despesa"""
        response = self.client.delete('/despesas/1/')
        self.assertEquals(response.status_code,
                          status.HTTP_204_NO_CONTENT)

    def test_put_despesa(self):
        """Teste para verificar a requisição PUT em uma despesa"""
        data = {
            'descricao_despesa': 'DespesaTeste',
            'valor_despesa': '100',
            'data_despesa': '2022-08-18',
            'categoria': 'A',
        }
        response = self.client.put('/despesas/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
