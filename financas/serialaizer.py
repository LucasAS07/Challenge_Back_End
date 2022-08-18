from rest_framework import serializers
from financas.models import Receita, Despesa
from rest_framework.exceptions import ValidationError


class ReceitaSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = '__all__'


class DespesaSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = '__all__'


class ListagemDespesas(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = ['descricao_despesa', 'valor_despesa', 'categoria']


class ListagemReceitas(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = ['descricao_receita', 'valor_receita']
