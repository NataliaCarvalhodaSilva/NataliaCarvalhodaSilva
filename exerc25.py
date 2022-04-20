# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE ELA TEM "SILVA" NO NOME.
nome = str(input('Qual é o seu nome completo? ')).strip()
nome = nome.title()
posição = str((nome.find('Silva')))
print('Seu nome tem Silva? ')
print(posição.isnumeric())
