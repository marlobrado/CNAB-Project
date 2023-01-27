from django.db import models

class Shop(models.Model):
    nomeDaLoja = models.CharField(max_length=25)
    donoDaLoja = models.CharField(max_length=25)


class Transactions(models.Model):
    tipo = models.CharField(max_length=30)
    data = models.CharField(max_length=16)
    valor = models.DecimalField(max_digits = 15, decimal_places = 2)
    cpf = models.CharField(max_length=12)
    cartao = models.CharField(max_length=12)
    hora = models.CharField(max_length=12)

    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="transacoes")

