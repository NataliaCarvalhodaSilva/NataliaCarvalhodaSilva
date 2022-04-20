# FAÇA UM PROGRAMA QUE LEIA 3 NÚMEROS E MOSTRE QUAL É O MAIOR E QUAL É O MENOR.

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite um número: '))
numero3 = int(input('Digite um número: '))
lista = [numero1, numero2, numero3]
print('O maior número da lista é ', max(lista))
print('O menor número da lista é ', min(lista))
