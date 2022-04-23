n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
# print('A soma vale {}'.format(n1+n2))
# print(f'A soma vale {n1+n2}')
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma é {}, a multiplicação é {} e a divisão é {}.'.format(s, m, d))
print(f'A soma é {s}, a multiplicação é {m} e a divisão é {d}.')
print('A divisão inteira é {} e a potência {}.'.format(di, e))
print(f'A divisão inteira é {di} e a potência {e}.')
# para nova linha \n  para na mesma linha , = end ' ' e dentro das aspas pode colocar qualquer sinal
# quando eu tenho uma divisão onde o resultado é infinito , 1,33333333333333333 POR EXEMPLO, posso colocar no print {:.3f}
