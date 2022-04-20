#FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO COM 5% DE DESCONTO.
p = float(input('Digite o valor do produto: '))
desc = p*5/100
print(f'Com 5% de desconto o produto fica no valor de R${p-desc:.2f}')
