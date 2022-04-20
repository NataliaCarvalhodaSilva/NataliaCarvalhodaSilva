# DESENVOLVA UM PROGRAMA QUE LEIA O NOME, IDADE E SEXO DE 4 PESSOAS.
# NO FINAL DO PROGRAMA, MOSTRE:
#       - A MÉDIA DE IDADE DO GRUPO
#       - O NOME DO HOMEM MAIS VELHO
#       - QUANTAS MULHERES TEM MENOS DE 20 ANOS

soma_de_idades = 0
media_de_idades = 0
idade_do_homem_mais_velho = 0
nome_do_homem_mais_velho = ''
total_de_mulheres_com_menos_de_vinte_anos = 0
for p in range (1, 5):
    print(f'-----PESSOA {p}-----')
    nome = str(input('Qual o nome da primeira pessoa? ')).strip().title()
    idade = int(input('Qual a idade da primeira pessoa? '))
    sexo = str(input('É do sexo masculino ou feminino? ')).strip().lower()
    soma_de_idades += idade
    # if p == 1 and sexo == 'masculino':
        # idade_do_homem_mais_velho = idade
        # nome_do_homem_mais_velho = nome
    if sexo == 'masculino' and idade > idade_do_homem_mais_velho:
        idade_do_homem_mais_velho = idade
        nome_do_homem_mais_velho = nome
    if sexo == 'feminino' and idade < 20:
        total_de_mulheres_com_menos_de_vinte_anos += 1
print(f'O homem mais velho do grupo é o {nome_do_homem_mais_velho} com {idade_do_homem_mais_velho} anos.')
print(f'O total de mulheres com menos de vinte anos foi {total_de_mulheres_com_menos_de_vinte_anos}.')
media_de_idades = soma_de_idades / 4
print(f'A média de idade do grupo é de {media_de_idades}.')
