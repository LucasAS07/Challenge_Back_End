from rest_framework import viewsets
from financas.models import Receita, Despesa
from financas.serialaizer import ReceitaSerialaizer, DespesaSerialaizer


class ReceitasViewSet(viewsets.ModelViewSet):
    """Exibe todas as receitas"""
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerialaizer


class DespesasViewSet(viewsets.ModelViewSet):
    """Exibe todas as despesas"""
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerialaizer
