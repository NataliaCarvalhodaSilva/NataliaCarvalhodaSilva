# CRIE UM PROGRAMA QUE LEIA O NOME E O PREÇO DE VÁRIOS PRODUTOS.
# O PROGRAMA DEVERÁ PERGUNTAR SE O USUÁRIO VAI CONTINUAR.
# NO FINAL, MOSTRE:
#      A) QUAL É O TOTAL GASTO;
#      B) QUANTOS PRODUTOS CUSTAM MAIS DE R$1000;
#      C) QUAL É O NOME DO PRODUTO MAIS BARATO.
print('-' * 20)
print('CADASTRE UM PRODUTO')
print('-' * 20)
total_da_compra = valor_maior_que_mil_reais = valor_do_produto_mais_barato = contador =0
produto_mais_barato = ''
while True:
    produto = str(input('Nome do produto: ')).strip().upper()
    preço = float(input('Digite o preço do produto: R$ '))
    contador += 1
    total_da_compra += preço
    if preço > 1000 :
        valor_maior_que_mil_reais += 1
    if contador == 1 or preço < valor_do_produto_mais_barato :
        valor_do_produto_mais_barato = preço 
        produto_mais_barato = produto
    resposta = ' '
    while resposta not in 'SN': 
        resposta = str(input('Deseja continuar? [S/N]  ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'O total da compra foi R${total_da_compra:.2f};\n{valor_maior_que_mil_reais} produto(s) com valor superior a R$1000.00;\nO produto mais barato foi {produto_mais_barato} e o valor do produto mais barato foi R${valor_do_produto_mais_barato}')

