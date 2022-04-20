# UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO.
# FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO O NOME DELES E ESCREVENDO O NOME DO ESCOLHIDO.
from random import choice 
aluno1 = input('Digite o nome do aluno que representa o número 1: ')
aluno2 = input('Digite o nome do aluno que representa o número 2: ')
aluno3 = input('Digite o nome do aluno que representa o número 3: ')
aluno4 = input('Digite o nome do aluno que representa o número 4: ')
sorteio = [aluno1, aluno2, aluno3, aluno4]
print(f'O aluno escolhido para apagar o quadro foi {choice(sorteio)}.')
