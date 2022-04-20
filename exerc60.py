# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO QUALQUER E MOSTRE O SEU FATORIAL.
# EX: 
#     5! = 5X4X3X2X1 = 120
import math
numero_escolhido = int(input('Digite um valor para saber o seu fatorial: '))
resultado = math.factorial(numero_escolhido)
print(f'O fatorial do número {numero_escolhido} é igual a {resultado}.')


c = numero_escolhido
print(f'Calculando {numero_escolhido}! ', end ='')
while c > 0:
    resultado = math.factorial(numero_escolhido)
    print(f'{c}', end = '')
    print(' x ' if c > 1 else ' = ', end = '')
    c -= 1
print(f'{resultado}')
