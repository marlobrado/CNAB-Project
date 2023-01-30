from .models import Shop, Transactions
from rest_framework import serializers


class ShopSerializer(serializers.Serializer):

    file = serializers.FileField(write_only=True)

    def create(self, validated_data):
        
        lines = validated_data["file"].readlines()

        for line in lines:
            typeLine = line.decode()[0:1]
            if typeLine == '2' or typeLine == '3' or typeLine == '9':
                valorTransacao = -1 * (int(line[9:19]) / 100)
            else:
                valorTransacao = int(line[9:19]) / 100

            if typeLine == '1':
                typeTransation = 'Débito'
            elif typeLine == '2':
                typeTransation = 'Boleto'
            elif typeLine == '3':
                typeTransation = 'Financiamento'
            elif typeLine == '4':
                typeTransation = 'Crédito'
            elif typeLine == '5':
                typeTransation = 'Recebimento Empréstimo'
            elif typeLine == '6':
                typeTransation = 'Vendas'
            elif typeLine == '7':
                typeTransation = 'Recebimento TED'
            elif typeLine == '8':
                typeTransation = 'Recebimento DOC'
            else:   
                typeTransation = 'Aluguel'
            shop = {
                "nomeDaLoja": line[62:81].strip().decode(),
                "donoDaLoja": line[48:62].strip().decode(),
            }
            trans = {
                "tipo": typeTransation,
                "data": line[1:9].decode(),
                "valor": valorTransacao,
                "cpf": line[19:30].decode(),
                "cartao": line[30:42].decode(),
                "hora": f'{line[42:44].decode()}:{line[44:46].decode()}:{line[46:48].decode()}',
            }
            shop_obj, created = Shop.objects.get_or_create(**shop)
            shop = Shop.objects.get(nomeDaLoja=line[62:81].strip().decode())
            Transactions.objects.create(shop=shop, **trans)
        return shop_obj

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ('id', 'tipo', 'data', 'valor', 'cpf', 'cartao', 'hora')

class ShopShowSerializer(serializers.ModelSerializer):
    saldo = serializers.SerializerMethodField()
    transacoes = TransactionsSerializer(many=True, read_only=True)
    
    class Meta:
        model = Shop
        fields = ('id','nomeDaLoja', 'donoDaLoja', 'saldo', 'transacoes')

    def get_saldo(self, obj):
        saldo = 0
        for transacao in obj.transacoes.all():
            if transacao.tipo == "2" or transacao.tipo == "3" or transacao.tipo == "9":
                saldo -= transacao.valor
            else:
                saldo += transacao.valor
        return saldo