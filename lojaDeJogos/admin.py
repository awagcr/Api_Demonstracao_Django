from django.contrib import admin
from lojaDeJogos.models import Cliente, Jogo, Distribuidora, Venda, Funcionario, ItensVenda


class Clientes(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'senha', 'endereco')
    list_display_links = ('nome', 'cpf')
    search_fields = ('nome', 'cpf',)
    list_per_page = 100


admin.site.register(Cliente, Clientes)


class Funcionarios(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'senha')
    list_display_links = ('nome', 'cpf')
    search_fields = ('nome', 'cpf',)
    list_per_page = 100


admin.site.register(Funcionario, Funcionarios)


class Distribuidoras(admin.ModelAdmin):
    list_display = ('nome',)
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_per_page = 100


admin.site.register(Distribuidora, Distribuidoras)


class Jogos(admin.ModelAdmin):
    list_display = ('nome', 'genero', 'distribuidora', 'qtd_estoque', 'preco')
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_per_page = 100


admin.site.register(Jogo, Jogos)


class Vendas(admin.ModelAdmin):
    list_display = ('funcionario', 'cliente', 'data')
    list_display_links = ('data',)
    search_fields = ('funcionario', 'cliente', 'data',)
    list_per_page = 100


admin.site.register(Venda, Vendas)


class ItensVendas(admin.ModelAdmin):
    list_display = ('venda', 'item', 'quantidade')
    list_display_links = ('venda', 'item')
    search_fields = ('venda',)
    list_per_page = 100


admin.site.register(ItensVenda, ItensVendas)
