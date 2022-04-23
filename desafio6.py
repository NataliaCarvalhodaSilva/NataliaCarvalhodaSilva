# CRIE UM ALGORITMO QUE LEIA UM NÚMERO E MOSTRE O SEU DOBRO, TRIPLO E RAIZ QUADRADA.
n = int(input('Digite um número: '))
d = n*2
t = n*3
r = n**(1/2)
print('O dobro do número {} é {}, o triplo é {} e a raiz quadrada é {}.'.format(n, d, t, r))
print(f'O dobro do número {n} é {d}, o triplo é {t} e a raiz quadrada é {r}.')
print(f'Analisando o número {n}, o dobro é igual a {n*2}, o triplo é {n*3} e a raiz quadrada é {n**(1/2)}.')
print('Analisando o número {}, o dobro é igual a {}, o triplo é {} e a raiz quadrada é {}.'.format(n, (n*2), (n*3), (n**(1/2))))
