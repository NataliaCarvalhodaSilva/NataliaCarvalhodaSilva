# CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR. (CONSIDERE US$1,00 = R$3,27).
n = float(input('Quanto em dinheiro você possui na carteira? '))
d = n * 3.27
print('A quantia de R${} em doláres equivale a UR${}.'.format(n, d))
print(f'A quantia  de R${n} em doláres equivale a UR${d}.')
