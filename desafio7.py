# DESENVOLVA UM PROGRAMA QUE LEIA AS DUAS NOTAS DE UM ALUNO, CALCULE E MOSTRE A SUA MÉDIA.
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2)/2
print('A primeira nota é {} e a segunda nota é {}. Então sua média é {}.'.format(n1, n2, m))
print(f'A primeira nota é {n1} e a segunda nota é {n2}. Então sua média é {m}.')
print('A primeira nota é {} e a segunda é {}. \nEntão sua média ficou {}.'.format(n1, n2, ((n1+n2)/2)))
print(f'A primeira nota é {n1} e a segunda {n2}. \nEntão sua média ficou {(n1+n2)/2:.2f}.')