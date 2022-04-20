# FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA, MOSTRANDO EM SEGUIDA O PRIMEIRO E O ÚLTIMO NOME SEPARADAMENTE.
# EX: Ana Maria de Souza    primeiro = Ana     último = Souza
n = str(input('Escreva seu nome completo: ')).strip().title()
nome = (n.split())
print(f'Muito prazer em te conhecer! Seu primeiro nome é {nome[0]}, e o último é {nome[len(nome)-1]}.')
