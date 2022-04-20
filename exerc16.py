#CRIE UM PROGRAMA QUE LEIA UM NÚMERO REAL QUALQUER PELO TECLADO E MOSTRE NA TELA SUA PORÇÃO INTEIRA.
# EXEMPLO: DIGITE UM NÚMERO: 6.127. O NÚMERO 6.127 TEM A PARTE INTEIRA 6.
from math import trunc 
n = float(input('Digite um número qualquer: '))
print(f'O número {n} possui a parte inteira de {trunc(n)}.')
