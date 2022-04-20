# ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR "PENSAR" EM UM NÚMERO INTEIRO ENTRE 0 E 5.
# PEÇA PARA O USUÁRIO TENTAR DESCOBRIR QUAL FOI O NÚMERO ESCOLHIDO PELO COMPUTADOR.
# O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUÁRIO VENCEU OU PERDEU.
import random
import time
computador = random.randint(0, 5) 
print('*'*30)
print('Eu vou pensar em um número de 0 a 5.')
print('*'*30)
jogador = int(input('Tente Adivinhar: '))
print('*'*30)
print('PROCESSANDO...')
time.sleep(5)
if jogador == computador:
    print('Parabéns, você me venceu!')
else:
    print(f'Teeeente outra vez! (Favor ler cantando!) O número sorteado foi {computador}.')
