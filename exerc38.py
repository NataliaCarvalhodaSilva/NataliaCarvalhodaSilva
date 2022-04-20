#  ESCREVA UM PROGRAMA QUE LEIA DOIS NÚMEROS INTEIROS E COMPARE-OS, MONSTRANDO NA TELA UMA MENSAGEM:
#      -O PRIMEIRO VALOR É MAIOR
#      -O SEGUNDO VALOR É MAIOR
#      -NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS
print('-' * 40)
primeiro_numero = int(input('Me fale um número: '))
segundo_numero = int(input('Agora outro número: '))
print('-' * 40)
numeros = ['primeiro_numero', 'segundo_numero']
if primeiro_numero > segundo_numero:
    print('O primeiro valor é maior!')
elif primeiro_numero < segundo_numero:
    print('O segundo valor é maior!')
elif primeiro_numero == segundo_numero:
    print('Não existe valor maior, os dois são iguais!')
