#FAÇA UM ALGORITMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO E MOSTRE SEU NOVO SALÁRIO, COM 15% DE AUMENTO.
s = float(input('Digite o salário: '))
a = s*15/100
print(f'O salário atual é R${s}, com o aumento de 15% ficará R${s+a:.2f}')