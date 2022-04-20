# DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTÂNCIA DE UMA VIAGEM EM KM.
# CALCULE O PREÇO DA PASSAGEM, COBRANDO R$0,50 PO KM PARA VIAGENS ATÉ 200 KM.
# E R$0,45 PARA VIAGENS MAIS LONGAS.
distancia = float(input('Qual foi a distância da viagem em km: '))
if distancia <= 200:
    valor1 = distancia * 0.5
    print(f'O valor a ser pago é de R${valor1}.')
else:
    valor2 = distancia * 0.45
    print(f'O valor a ser pago é de R${valor2:.2f}.')
