# CRIE UM PROGRAMA QUE SIMULE O FUNCIONAMENTO DE UM CAIXA ELETRÔNICO.
# NO INÍCIO, PERGUNTE AO USUÁRIO QUAL SERÁ O VALOR A SER SACADO (NÚMERO INTEIRO).
# E O PROGRAMA VAI INFORMAR QUANTAS CÉDULAS DE CADA VALOR SERÃO ENTREGUES.
#    OBS.: CONSIDERE QUE O CAIXA POSSUI CÉDULAS DE R$50 R$20 R$10 E R$1.
from math import trunc

print('-' * 40)
print('BEM VINDO AO NATIBANK')
print('-' * 40)
valor_do_saque = int(input('Digite o valor do saque: R$'))
cedulas = [50, 20, 10, 1]
resto = valor_do_saque
for contagem in cedulas :
    total_de_cedulas = trunc(resto / contagem)
    resto = resto - total_de_cedulas * contagem
    if total_de_cedulas > 0:
        print(f'O total de cédulas de R${contagem} -> {total_de_cedulas}')

print('-' * 40)
print('OBRIGADO POR UTILIZAR NOSSO BANCO!\nVOLTE SEMPRE!')

# total_de_cedulas_de_50 = trunc(valor_do_saque / 50)
# resto_50 = valor_do_saque - total_de_cedulas_de_50 * 50
# total_de_cedulas_de_20 = trunc(resto_50 / 20)
# resto_20 = resto_50 - total_de_cedulas_de_20 * 20
# total_de_cedulas_de_10 = trunc(resto_20 / 10)
# total_de_cedulas_de_1 = resto_20 - total_de_cedulas_de_10 * 10