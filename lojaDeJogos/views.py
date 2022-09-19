from rest_framework import viewsets, generics

from lojaDeJogos.models import Cliente, Jogo, Distribuidora, Venda, Funcionario, ItensVenda
from lojaDeJogos.serializer import ClienteSerializer, JogoSerializer, DistribuidoraSerializer, FuncionarioSerializer, \
    VendaSerializer, ItensVendaSerializer, ListaComprasClienteSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class ClientesViewSet(viewsets.ModelViewSet):
    """Exibindo todos clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class JogosViewSet(viewsets.ModelViewSet):
    """Exibindo todos clientes"""
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer


class DistribuidorasViewSet(viewsets.ModelViewSet):
    """Exibindo todos clientes"""
    queryset = Distribuidora.objects.all()
    serializer_class = DistribuidoraSerializer


class VendasViewSet(viewsets.ModelViewSet):
    """Exibindo todos clientes"""
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
    http_method_names = ['get', ]
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class FuncionariosViewSet(viewsets.ModelViewSet):
    """Exibindo todos clientes"""
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ItensVendasViewSet(viewsets.ModelViewSet):
    """Exibindo todos clientes"""
    queryset = ItensVenda.objects.all()
    serializer_class = ItensVendaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaComprasClientes(generics.ListAPIView):
    """Listando as compras de um cliente"""
    def get_queryset(self):
        queryset = Venda.objects.filter(cliente_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaComprasClienteSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
