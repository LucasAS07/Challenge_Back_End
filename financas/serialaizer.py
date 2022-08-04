from rest_framework import serializers
from financas.models import Receita


class ReceitaSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = ['id', 'descricao_receita', 'valor_receita', 'data_receita']
