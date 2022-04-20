# CRIE UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA SE ELE É PAR OU ÍMPAR.
numero = int(input('Insira um número sem vírgulas: '))
if (numero % 2) == 0:
# O RESULTADO DE QUALQUER NÚMERO PAR POR 2 É 0
# O RESULTADO DE QUALQUER NÚMERO ÍMPAR POR 2 É 1
    print(f'O número {numero} é par!')
else:
    print(f'O número {numero} é ímpar!')
