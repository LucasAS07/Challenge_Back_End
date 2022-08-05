from rest_framework import serializers
from financas.models import Receita, Despesa


class ReceitaSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = ['id', 'descricao_receita', 'valor_receita', 'data_receita']


class DespesaSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = ['id', 'descricao_despesa', 'valor_despesa', 'data_despesa']

