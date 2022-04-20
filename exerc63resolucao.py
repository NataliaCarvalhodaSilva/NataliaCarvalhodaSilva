# ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO N INTEIRO QUALQUER E MOSTRE NA TELA:
#        -OS N PRIMEIROS ELEMENTOS DE UMA SEQUÊNCIA FIBONACCI.
# EX: 0 -> 1 -> 2 -> 3 -> 5 -> 8 -> 13 -> 21 -> 34
# fn = fn - 1 + fn - 2
# acima é a fórmula da Sequência Fibonacci
print('-' * 5, 'SEQUÊNCIA FIBONACCI', '-' * 5)
numero = int(input('Quantos termos você quer mostrar? '))
primeiro_termo = 0
segundo_termo = 1
print(f'{primeiro_termo} - > {segundo_termo}', end = '')
contador = 3
while contador <= numero:
    terceiro_termo = primeiro_termo + segundo_termo
    print(f' -> {terceiro_termo}', end = '')
    primeiro_termo = segundo_termo
    segundo_termo = terceiro_termo
    contador += 1
print(' -> FIM ')
