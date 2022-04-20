import random
numero = int(input('Escolha um número de 0 a 5: '))
computador = random.randrange(0, 5)
if (numero+computador) % 2 == 0 :
    print('Você ganhou!', numero)
else:
    print('O computador ganhou!', computador)
