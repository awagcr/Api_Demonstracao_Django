"""api_loja_de_jogos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from lojaDeJogos.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('clientes', ClientesViewSet, basename='Clientes')
router.register('jogos', JogosViewSet, basename='Jogos')
router.register('funcionarios', FuncionariosViewSet, basename='Funcionarios')
router.register('distribuidoras', DistribuidorasViewSet, basename='Distribuidoras')
router.register('vendas', VendasViewSet, basename='Vendas')
router.register('itensVendas', ItensVendasViewSet, basename='Itens de Vendas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('cliente/<int:pk>/compras', ListaComprasClientes.as_view())
]
