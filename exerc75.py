# DESENVOLVA UM PROGRAMA QUE LEIA QUATRO VALORES PELO TECLADO E GUARDE-OS EM UMA TUPLA. 
# NO FINAL, MOSTRE:
#        a) QUANTAS VEZES APARECEU O VALOR 9;
#        b) EM QUE POSIÇÃO FOI DIGITADO O PRIMEIRO VALOR 3;
#        c) QUAIS FORAM OS NÚMEROS PARES.

numero1 = int(input('Digite um valor: '))
numero2 = int(input('Digite um valor: '))
numero3 = int(input('Digite um valor: '))
numero4 = int(input('Digite um valor: '))
lista = (numero1, numero2, numero3, numero4)
contador = 0
print(f'Quantas vezes aparece o número 9: {lista.count(9)}')
print(f'O número 3 apareceu primeiro na posição {lista.index(3)}.')
for c in lista:
    if c % 2 == 0:
        contador += 1
        print(f'O número {c} é par.')
print(f'{contador} número(s) par(es).')
