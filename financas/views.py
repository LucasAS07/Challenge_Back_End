from rest_framework import viewsets
from financas.models import Receita
from financas.serialaizer import ReceitaSerialaizer


class ReceitasViewSet(viewsets.ModelViewSet):
    """Exibe todas as receitas"""
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerialaizer
