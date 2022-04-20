# FAÇA UM PROGRAMA QUE MOSTRE A TABUADA DE VÁRIOS NÚMEROS, UM DE CADA VEZ, PARA CADA VALOR DIGITADO PELO USUÁRIO.
# O PROGRAMA SERÁ INTERROMPIDO QUANDO O NÚMERO SOLICITADO FOR NEGATIVO.

print('-' * 5, 'TABUADA', '-' * 5)
print('Para encerrar, digite um número menor que 0.')
while True:
    numero = int(input('Digita um valor para ver sua tabuada: '))
    if numero < 0:
        break
    for tabuada in range (1, 11):
        print(numero, 'x' , tabuada, '=' , numero * tabuada)
print('ACABOU!')
