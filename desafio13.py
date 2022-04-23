# FAÇA UM ALGORITMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO E MOSTRE SEU NOVO SALÁRIO, COM 15% DE AUMENTO.
s = float(input('Digite o salário do funcionário: '))
a = s * 0.15 
ns = s + a
print ('O salário do funcionário é igual a R${}, e com o aumento ficou R${}.'.format(s, ns))
print (f'O salário do funcionário é igual a R${s}, e com o aumento ficou R${ns}.')
