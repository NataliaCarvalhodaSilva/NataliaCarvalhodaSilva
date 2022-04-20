# FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACORDO COM A SUA IDADE:
#      -SE ELE AINDA VAI SE ALISTAR NO SERVIÇO MILITAR.
#      -SE É A HORA DE SE ALISTAR.
#      -SE JÁ PASSOU DO TEMPO DO ALISTAMENTO.
# SEU PROGRAMA TAMBÉM DEVERÁ MOSTRAR O TEMPO QUE FALTA OU QUE PASSOU DO PRAZO.
from datetime import date
ano_atual = date.today().year
ano_de_nascimento = int(input('Qual é o ano em que você nasceu?(Digitar os 4 números.) '))
idade = ano_atual - ano_de_nascimento
if idade < 18:
    quanto_ainda_falta = 18 - idade
    ano_de_alistamento = ano_atual + quanto_ainda_falta 
    print(f'''Logo você irá se alistar! Falta {quanto_ainda_falta} para o seu alistamento. 
    Que será em {ano_de_alistamento}.''')

elif idade == 18:
    print('Está na hora de se alistar! Boa sorte!')

elif idade > 18:
    quanto_ja_passou = idade - 18
    ano_de_alistamento = ano_atual - quanto_ja_passou
    print(f'Já passou {quanto_ja_passou} anos do tempo para se alistar, que foi no ano {ano_de_alistamento}!')
print('-' * 40)
print('Obrigada pelas informações!')