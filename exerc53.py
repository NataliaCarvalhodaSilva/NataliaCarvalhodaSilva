# CRIE UM PROGRAMA QUE LEIA UMA FRASE QUALQUER E DIGA SE ELA É UM PALÍNDROMO, DESCONSIDERANDO OS ESPAÇOS.
p = input('Digite algo: ').replace(' ', '').upper()
lista = list(p)
palavra_invertida = ''
for c in reversed(lista):
    palavra_invertida = palavra_invertida + c
if p == palavra_invertida:
    print(f'A palavra {p} é um palíndromo!')
else:
    print(f'A palavra {p} não é um palíndromo. {palavra_invertida}')
