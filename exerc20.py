# O MESMO PROFESSOR DO DESAFIO ANTERIOR QUER SORTEAR A ORDEM DE APRESENTAÇÃO DE TRABALHOS DOS ALUNOS.
# FAÇA UM PROGRAMA QUE LEIA O NOME DOS QUATRO ALUNOS E MOSTRE A ORDEM SORTEADA.
from random import shuffle
aluno1 = input('Digite o nome do aluno que representa o número 1: ')
aluno2 = input('Digite o nome do aluno que representa o número 2: ')
aluno3 = input('Digite o nome do aluno que representa o número 3: ')
aluno4 = input('Digite o nome do aluno que representa o número 4: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)
print(f'A ordem de alunos a apresentarem é {alunos}.')
# O COMANDO SHUFFLE DIFERENTEMENTE DO CHOICES NÃO RETORNA NADA, ELE APENAS CUMPRE UMA FUNÇÃO.
