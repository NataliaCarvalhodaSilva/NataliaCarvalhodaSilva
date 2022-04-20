# MELHORE O JOGO DESAFIO 028 ONDE O COMPUTADOR VAI "PENSAR" EM UM NÚMERO ENTRE 0 E 10.
# SÓ QUE AGORA O JOGADOR VAI TENTAR ADIVINHAR ATÉ ACERTAR.
# MOSTRANDO NO FINAL QUANTOS PALPITES FORAM NECESSÁRIOS PARA VENCER.
import random
computador = random.randint(0, 10) 
print('*'*30)
print('Eu vou pensar em um número de 0 a 10.')
print('*'*30)
jogador = 0
jogadas = 0
while jogador != computador:
    jogador = int(input('Tente Adivinhar: '))
    jogadas += 1
    if computador > jogador:
        print('Mais... ')
    if jogador > computador:
        print('Menos... ')
    if jogador == computador:
        print(f'Foram {jogadas} jogadas. O número sorteado foi {computador}.')
