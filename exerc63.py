# ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO N INTEIRO QUALQUER E MOSTRE NA TELA:
#        -OS N PRIMEIROS ELEMENTOS DE UMA SEQUÊNCIA FIBONACCI.
# EX: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
# fn = fn - 1 + fn - 2
# acima é a fórmula da Sequência Fibonacci
print('-' * 5 , 'SEQUÊNCIA FIBONACCI', '-' * 5)
contador = 0
penultimo = 0
ultimo = 1
n = int(input('Quantos termos você quer mostrar: '))
if n == 1:
    print(penultimo)
elif n == 2:
    print(penultimo)
    print(ultimo)
elif n > 2:
    print(penultimo)
    print(ultimo)
    contador = 2
    while contador < n:
        novo_numero = ultimo + penultimo
        print(novo_numero)
        penultimo = ultimo
        ultimo = novo_numero
        contador += 1
