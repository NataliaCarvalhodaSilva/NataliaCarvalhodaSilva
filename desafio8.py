# ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM CENTÍMETROS E MILÍMETROS.
n = float(input('Medida em metros: '))
c = n * 100
m = n * 1000
print(f'O tamanho é {c} centímetros e {m} milímetros.')
print('O tamanho é {} cm e {} mm.'.format(c, m))
