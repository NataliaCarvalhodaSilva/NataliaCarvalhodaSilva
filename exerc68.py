# FAÇA UM PROGRAMA QUE JOGUE PAR OU ÍMPAR COM O COMPUTADOR.
# O JOGO SÓ SERÁ INTERROMPIDO QUANDO O JOGADOR PERDER, MOSTRANDO O TOTAL DE VITÓRIAS CONSECUTIVAS QUE ELE CONQUISTOU NO FINAL DO JOGO.

import random 
contador = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = random.randint(0,11)
    total = jogador + computador
    escolha = str(input('Você escolhe PAR ou ÍMPAR? [P/I]')).strip().upper()[0]
    if escolha == 'P' and total % 2 == 0:
        print(f'Você Ganhou! O total foi {total}, eu escolhi {computador}.')
        contador += 1
    elif escolha == 'I' and total % 2 == 1:
        print(f'Você ganhou! O total foi {total}, eu escolhi {computador}.')
        contador += 1
    else:
        break

print(f'Você ganhou {contador} rodadas!\nMas agora você PERDEU! A soma foi {total}, eu escolhi {computador}!')
