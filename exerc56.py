# DESENVOLVA UM PROGRAMA QUE LEIA O NOME, IDADE E SEXO DE 4 PESSOAS.
# NO FINAL DO PROGRAMA, MOSTRE:
#       - A MÉDIA DE IDADE DO GRUPO
#       - O NOME DO HOMEM MAIS VELHO
#       - QUANTAS MULHERES TEM MENOS DE 20 ANOS
print('Pense em 4 pessoas, e em seguida responda:')
print('-' * 40)
nome1 = str(input('Qual o nome da primeira pessoa? '))
idade1 = int(input('Qual a idade da primeira pessoa? '))
sexo1 = str(input('É do sexo masculino ou feminino? '))
print('-' * 40)
nome2 = str(input('Qual o nome da segunda pessoa? '))
idade2 = int(input('Qual a idade da segunda pessoa? '))
sexo2 = str(input('É do sexo masculino ou feminino? '))
print('-' * 40)
nome3 = str(input('Qual o nome da terceira pessoa? '))
idade3 = int(input('Qual a idade da terceira pessoa? '))
sexo3 = str(input('É do sexo masculino ou feminino? '))
print('-' * 40)
nome4 = str(input('Qual o nome da quarta pessoa? '))
idade4 = int(input('Qual a idade da quarta pessoa? '))
sexo4 = str(input('É do sexo masculino ou feminino? '))
print('-' * 40)
pessoas = {
   'pessoa1': {
        'nome': nome1,
        'idade': idade1,
        'sexo': sexo1
    },
    'pessoa2': {
        'nome': nome2,
        'idade': idade2,
        'sexo': sexo2
    },
    'pessoa3': {
        'nome': nome3,
        'idade': idade3,
        'sexo': sexo3
    },
    'pessoa4': {
        'nome': nome4,
        'idade': idade4,
        'sexo': sexo4
    }
}
media_de_idades = (idade1 + idade2 + idade3 + idade4) /4
maior_idade = 0
menor_que_20 = 0
for c in pessoas:
    if pessoas[c].get('sexo') == 'masculino' and pessoas[c].get('idade') >= maior_idade:
        maior_idade = pessoas[c].get('idade')
for c in pessoas:
    if pessoas[c].get('sexo') == 'masculino' and pessoas[c].get('idade') == maior_idade:
        print( f"O {pessoas[c].get('nome')} é  mais velho, com {pessoas[c].get('idade')}")
for c in pessoas:
    if pessoas[c].get('sexo') == 'feminino' and pessoas[c].get('idade') < 20:
        menor_que_20 = menor_que_20 + 1
print(f'{menor_que_20} mulher(es) tem menos de 20 anos.')
print(f'A média de idades é igual a {media_de_idades}.')
