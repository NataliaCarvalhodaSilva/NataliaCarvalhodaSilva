#  ESCREVA UM PROGRAMA PARA APROVAR O EMPRÉSTIMO BANCÁRIO PARA A COMPRA DE UMA CASA.
#  O PROGRAMA VAI PERGUNTAR O VALOR DA CASA, O SALÁRIO DO COMPRADOR E EM QUANTOS ANOS ELE VAI PAGAR.
#  CALCULE O VALOR DA PRESTAÇÃO MENSAL, SABENDO QUE ELA NAO PODE EXCEDER 30% DO SALÁRIO.
#  OU ENTÃO O EMPRÉSTIMO SERÁ NEGADO.
print('-' * 40)
valor_da_casa = float(input('Insira o valor do imóvel: R$'))
salario_do_comprador = float(input('Qual o salário do comprador: R$'))
tempo_para_pagar = int(input('Em quanto tempo pretende pagar as parcelas? '))
# cálculo para a parcela
valor_maximo = salario_do_comprador * (30/100)
# calculando a parcela referente ao tempo que comprador quer pagar
total_de_meses = tempo_para_pagar * 12 
valor_da_parcela = valor_da_casa / total_de_meses
print('-' * 40)
if valor_da_parcela <= valor_maximo:
    print(f'O empréstimo foi APROVADO! A parcela ficou em R${valor_da_parcela:.2f} e o valor máximo para pagamento é R${valor_maximo}.')
else:
    print(f'O empréstimo foi NEGADO! Parcela de R${valor_da_parcela:.2f} e o valor máximo para pagamento é R${valor_maximo}.')
