# CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO.
# O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR O VALOR 999, QUE É A CONDIÇÃO DE PARADA.
# NO FINAL, MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS E QUAL FOI A SOMA ENTRE ELES.
# DESCONSIDERANDO O FLAG.
numero = soma = contador = 0
from time import sleep
print('*' * 4, 'CONTADOR DE NÚMEROS', '*' * 4)
print('[999 é a condição de parada]')
while True:
    numero = int(input('Digite um número:  ')) 
    if numero == 999:
        break
    soma += numero
    contador += 1
print('ANALISANDO...')
sleep(2)
print(f'Foram digitados {contador} números, e sua soma é igual a {soma}.')
