#APRENDENDO A IMPORTAR BIBLIOTECAS DE PYTHON:
#COMANDO IMPORT, EXEMPLOS A SEGUIR COM A BIBLIOTECA MATH
#   IMPORT MATH ---IMPORTA A BIBLIOTECA COMPLETA 
#   FROM MATH IMPORT ________ --- IMPORTA UMA FUNCIONALIDADE ESPECIFICA DA BIBLIOTECA
import math
import emoji
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raíz quadrada de {num} é igual a {math.floor(raiz):.2f}.')
#NO CASO ADICIONEI AO COMANDO FORMAT A FUNCIONALIDADE FLOOR, IMPORTADA DA BIBLIOTECA MATH
#     SERVE PARA ARREDONDAR UM NÚMERO PARA BAIXO, E CEIL ARREDONDA PARA CIMA.
from math import sqrt, floor, ceil
num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f'A raíz quadrada do número {num} é igual a {floor(raiz)}')
print(emoji.emojize("Python is fun :red_heart:",variant="emoji_type"))