from django.db import models

# Create your models here.


class Distribuidora(models.Model):
    nome = models.CharField(max_length=150, null=False)

    def __str__(self):
        return self.nome


class Jogo(models.Model):
    nome = models.CharField(max_length=150, null=False)
    genero = models.CharField(max_length=30, null=False)
    distribuidora = models.ForeignKey(
        Distribuidora,
        on_delete=models.RESTRICT,
    )
    qtd_estoque = models.IntegerField()
    preco = models.DecimalField(
        decimal_places=2,
        max_digits=20
    )

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=150, null=False)
    cpf = models.CharField(max_length=11, null=False)
    senha = models.CharField(max_length=80, null=True)
    endereco = models.TextField()

    def __str__(self):
        return self.nome


class Funcionario (models.Model):
    nome = models.CharField(max_length=150, null=False)
    cpf = models.CharField(max_length=11, null=False)
    senha = models.CharField(max_length=80, null=True)

    def __str__(self):
        return self.nome


class Venda (models.Model):
    funcionario = models.ForeignKey(
        Funcionario,
        on_delete=models.RESTRICT
    ),
    cliente = models.IntegerField()
    data = models.DateField()

    def __str__(self):
        return self.data


class ItensVenda(models.Model):
    venda = models.ForeignKey(
        Venda,
        on_delete=models.CASCADE
    )
    item = models.ForeignKey(
        Jogo,
        on_delete=models.RESTRICT
    )
    quantidade = models.IntegerField()


