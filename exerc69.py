# CRIE UM PROGRAMA QUE LEIA A IDADE E O SEXO DE VÁRIAS PESSOAS.
# A CADA PESSOA CADASTRADA, O PROGRAMA DEVERÁ PERGUNTAR SE O USUÁRIO QUER OU NÃO CONTINUAR.
# NO FINAL, MOSTRE:
#      A) QUANTAS PESSOAS TEM MAIS DE 18 ANOS;
#      B) QUANTOS HOMENS FORAM CADASTRADOS;
#      C) QUANTAS MULHERES TEM MENOS DE 20 ANOS.
print('-' * 20)
print('CADASTRE UMA PESSOA')
print('-' * 20)
pessoas_com_mais_de_dezoito_anos = 0
quantos_m_cadastrados = 0
quantas_mulheres_com_menos_de_vinte_anos = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Digite o sexo: [F/M] ')).strip().upper()[0]
    resposta = ' '
    while resposta not in 'SN': 
        resposta = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if idade >= 18 :
        pessoas_com_mais_de_dezoito_anos += 1
    if sexo == 'M':
        quantos_m_cadastrados += 1
    if sexo == 'F' and idade < 20 :
        quantas_mulheres_com_menos_de_vinte_anos += 1
    if resposta == 'N':
        break

print(f'São {pessoas_com_mais_de_dezoito_anos} pessoas com mais de 18 anos;\nSão {quantos_m_cadastrados} homens cadastrados;\nE {quantas_mulheres_com_menos_de_vinte_anos} mulheres com menos de 20 anos.')
