# ESCREVA UM PROGRAMA QUE PERGUNTE O SALÁRIO DE UM FUNCIONÁRIO E CALCULE O VALOR DO SEU AUMENTO.
# PARA SALÁRIOS SUPERIORES A R$1.250,00, CALCULE UM AUMENTO DE 10%.
# PARA OS INFERIORES OU IGUAIS, O AUMENTO É DE 15%.
salario = float(input('Qual é o salário do funcionário? '))
if salario > 1250:
    porcentagem = salario * (10/100)
    aumento = salario + porcentagem 
    print(f'O valor atualizado do salário é {aumento:.2f}.')

else: 
    porcentagem2 = salario * (15/100)
    aumento2 = salario + porcentagem2
    print(f'O valor atualizado do salário é R${aumento2:.2f}.')

