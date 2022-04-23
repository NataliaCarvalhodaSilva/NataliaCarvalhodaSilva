# FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO, COM 5% DE DESCONTO.
p = float(input('Digite o preço do produto: '))
d = p * 0.05
np = p - d
print('O valor do produto é R${}, acrescentando 5 de desconto ficará R${}.'.format(p, np))
print(f'O valor do produto é R${p}, acrescentando 5% de desconto ficara R${np}.')
