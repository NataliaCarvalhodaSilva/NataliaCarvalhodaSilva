#   A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM ATLETA E MOSTRE SUA CATEGORIA, DE ACORDO COM A IDADE:
#   -ATÉ 9 ANOS: MIRIM
#   -ATÉ 14 ANOS: INFANTIL
#   -ATÉ 19 ANOS: JUNIOR
#   -ATÉ 20: SÊNIOR
#   -ACIMA: MASTER
from datetime import date
ano_atual = date.today().year
ano_de_nascimento = int(input('Qual é o ano em que você nasceu?(Digitar os 4 números.) '))
idade = ano_atual - ano_de_nascimento
print(f'Você tem {idade} anos.')
print('-' * 40)
if idade <= 9:
    print('Você faz parte da turma MIRIM! ')

elif idade <= 14:
    print('Você faz parte da turma INFANTIL!')

elif idade <= 19:
    print('Você faz parte da turma JUNIOR!')

elif idade <= 20:
    print('Você faz parte da turma SÊNIOR!')

elif idade > 20:
    print('Você faz parte da turma MASTER!')

print('-' * 40)
print('Bem vindo!')
