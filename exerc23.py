# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO DE 0 A 9999 E MOSTRE NA TELA CADA UM DOS DÍGITOS SEPARADOS.
# EX: 'Digite um número:' 1834
# #      Unidade: 4 dezena: 3  centena: 8  milhar: 1
# número = int(input('Digite um número de 0 a 9999: '))
# número =(len(número.replace(' ', '')))
# print(len(número(0))) 
# print(len(número(1)))
# print(len(número(2)))
# print(len(número(3)))
# print(len(número[1]))
# como eu fiz não rodou, resolução da aula
num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {num}.')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
