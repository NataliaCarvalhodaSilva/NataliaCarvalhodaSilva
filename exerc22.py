# CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
# *O nome com todas as letras maiúsculas
# *O nome com todas as letras minúsculas
# *Quantas letras ao todo (sem considerar espaços)
# *Quantas letras tem o primeiro nome
nome = input('Digite seu nome completo: ').strip()
print(nome.upper())
print(nome.lower())
n = nome.split()
print(len(n[0]))