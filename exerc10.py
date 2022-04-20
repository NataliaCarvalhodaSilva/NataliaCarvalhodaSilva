#FAÇA UM PROGRAMA QUE LEIA QUANTO DE DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR.
#CONSIDERE US$1,00 = R$3,27
r = float(input('Quanto em dinheiro você possui na carteira? R$'))
d = r / 3.27
print(f'A quantia de R${r:.2f} em dólares é igual a UR${d:.2f}.')
