# CRIE UM PROGRAMA QUE VAI GERAR CINCO NÚMEROS ALEATÓRIOS E COLOCAR EM TUPLA.
# DEPOIS DISSO, MOSTRE A LISTAGEM DE NÚMEROS GERADOS E TAMBÉM INDIQUE O MENOR E O MAIOR VALOR QUE ESTÃO NA TUPLA.
from random import randint
maior_numero = menor_numero = 0
for c in range(0,5):
    numeros = (randint(1,10))
    print(numeros, end = ' ')
    if numeros > maior_numero:
        maior_numero = numeros
    if c == 1 :
        menor_numero = numeros
    elif numeros < menor_numero:
        menor_numero = numeros
print(f'O maior número é {maior_numero}.')
print(f'O menor número é {menor_numero}.')
print('ACABOU!')
