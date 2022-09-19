import datetime

from lojaDeJogos.models import Venda, Funcionario, Cliente, ItensVenda


def crie_venda(id_cliente, id_vendedor, itens=[]):
    cliente = Cliente.objects.filter(cliente_id=id_cliente)
    vendedor = Funcionario.objects.filter(funcionario_id=id_vendedor)
    venda = Venda(cliente=cliente, funcionario=vendedor, data=datetime.datetime.now())
    Venda.save()
    for item in itens:
        itens_vendidos = ItensVenda(item_id=item.item, quantidade=item.quantidade)
        itens_vendidos.save()
