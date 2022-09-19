from rest_framework import serializers
from lojaDeJogos.models import Cliente, Jogo, Distribuidora, Venda, Funcionario, ItensVenda


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogo
        fields = '__all__'


class DistribuidoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distribuidora
        fields = '__all__'


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'


class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        exclude = []


class ItensVendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItensVenda
        exclude = []


class ListaComprasClienteSerializer(serializers.ModelSerializer):
    venda_data = serializers.ReadOnlyField(source='venda.data')

    class Meta:
        model = Venda
        fields = ['venda_data']
