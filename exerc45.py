#   CRIE UM PROGRAMA QUE FAÇA O COMPUTADOR JOGAR JOKENPÔ COM VOCÊ.
import random
from time import sleep

jogador = str(input('''Escolha PEDRA, PAPEL ou TESOURA... 
O que você escolhe? ''')).lower().strip()
opcoes = ['pedra', 'papel', 'tesoura']
computador = random.choice(opcoes)
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
if jogador == 'pedra' and computador == 'tesoura' or jogador == 'tesoura' and computador == 'papel' or jogador == 'papel' and computador == 'pedra':
    print(f'VOCÊ ME VENCEU! Escolhi {computador}.')

elif computador == 'pedra' and jogador == 'tesoura' or computador == 'tesoura' and jogador == 'papel' or computador == 'papel' and jogador == 'pedra':
    print(f'VOCÊ PERDEU! Minha escolha foi {computador}.')

elif jogador == computador:
    print(f'Empatamos! Escolhi {computador}.')

else:
    print('Não entendi, tente de novo!')
