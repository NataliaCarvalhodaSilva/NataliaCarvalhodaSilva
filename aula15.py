# contador = n = 0
# while contador <= 10:
#     print(contador, ' -> ', end = '')
#     contador += 1
# print('ACABOU')
# n = s = 0
# while n != 999:
#     n = int(input('Digite um número: '))
#     s += n
# print(f'A soma é igual a {s}')
#  ACIMA TEMOS O EXEMPLO DE UM WHILE USANDO FLAGS
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(s)
# ACIMA TENHO O EXEMPLO COM O COMANDO BREAK
