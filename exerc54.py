# CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE SETE PESSOAS.
# NO FINAL, MOSTRE QUANTAS PESSOAS AINDA NÃO ATINGIRAM A MAIORIDADE E QUANTAS JÁ SÃO MAIORES.
# CONSIDERANDO A MAIORIDADE AOS 21 ANOS.
from datetime import date
ano_atual = date.today().year
total_maiores = 0
total_menores = 0
# para soma de todos os maiores e todos os menores de idade
for pessoas in range (1,8):
    ano_de_nascimento = int(input(f'Insira um ano de nascimento da {pessoas} pessoa: '))
    idade = ano_atual - ano_de_nascimento
    if idade >= 21 :
        total_maiores += 1
    else:
        total_menores += 1
print(f'Ao todo tivemos {total_maiores} pessoas que já atingiram a maioridade!')
print(f'Ao todo tivemos {total_menores} pessoas que não atingiram a maioridade!')
