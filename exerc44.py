#   ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO, CONSIDERANDO O SEU PREÇO NORMAL E CONDIÇÃO DE PAGAMENTO:
#    -À VISTA NO DINHEIRO/CHEQUE: 10% DE DESCONTO
#    -À VISTA NO CARTÃO: 5% DE DESCONTO
#    -EM ATÉ 2X NO CARTÃO: PREÇO NORMAL
#    -3X OU MAIS NO CARTÃO: 20% DE JUROS
print('-' * 40)
preço_inicial = float(input('Qual o preço do(s) produto(s): '))
forma_de_pagamento = str(input('Qual a forma de pagamento? ')).lower()
print('-' * 40)
if forma_de_pagamento == 'dinheiro' or forma_de_pagamento == 'cheque':
    desconto = preço_inicial * (10/100)
    preço_final = preço_inicial - desconto
    print(f'O valor a ser pago é R${preço_final}.')

if forma_de_pagamento == 'cartao':
    pagamento = input('Deseja parcelar? ').lower()
    if pagamento == 'não':
        desconto = preço_inicial * (5/100)
        preço_final = preço_inicial - desconto
        print(f'O valor a ser pago é R${preço_final}.')
    if pagamento == 'sim':
       parcelas = int(input('Em quantas parcelas? '))
       if parcelas == 2:
            valor_parcela = preço_inicial / parcelas
            print(f'O valor a ser pago é R${preço_inicial}. Em {parcelas} fica R${valor_parcela} cada parcela.')
       elif parcelas >= 3:
        juros = preço_inicial * (20/100)
        preço_final = preço_inicial + juros
        valor_parcela = preço_final / parcelas
        print(f'O valor a ser pago é R${preço_final}. Em {parcelas} fica R${valor_parcela} cada parcela.')
