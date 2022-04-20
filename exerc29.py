# ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO.
# SE ELE ULTRAPASSAR 80 KM/H, MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO.
# A MULTA VAI CUSTAR R$7,00 POR CADA KM ACIMA DO LIMITE.

velocidade = float(input('Insira a velocidade: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você ultrapassou a velocidade permitida 80km/h! O valor da multa é R${multa:.2f}.')
else :
    print('Você não possuiu multas.')
print('*'*90)
print('Dirija com segurança!')
