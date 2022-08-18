from django.contrib import admin
from django.urls import path, include
from financas.views import ReceitasViewSet, DespesasViewSet, ListaDespesas, ListaReceitas, ResumoDoMes
from rest_framework import routers

router = routers.DefaultRouter()
router.register('receitas', ReceitasViewSet, basename='Receitas')
router.register('despesas', DespesasViewSet, basename='Despesas')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('despesas/<int:month>/<int:year>/', ListaDespesas.as_view()),
    path('receitas/<int:month>/<int:year>/', ListaReceitas.as_view()),
    path('resumo/<int:mes>/<int:ano>/', ResumoDoMes.as_view()),
]
