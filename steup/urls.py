from django.contrib import admin
from django.urls import path, include
from financas.views import ReceitasViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('receitas', ReceitasViewSet, basename='Receitas')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
