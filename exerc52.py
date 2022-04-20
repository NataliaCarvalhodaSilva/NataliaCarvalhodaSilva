# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E DIGA SE ELE É OU NÃO UM NÚMERO PRIMO.
# Números primos são divisíveis apenas por 1 e por ele mesmo.
numero = int(input('Digite um número: '))
tot = 0
for c in range (1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end = ' ')
        tot += 1
    else: 
        print('\033[31m', end = ' ')
    print(f'{c}', end = '')
print(f'\n\033[mO número {numero} foi divisível {tot} vezes.')
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO é primo!')

# if numero % 1 == 0 and numero % numero == 0 and numero % 2 == 1:
#     print(f'O número {numero} é primo.')
# else:
#     print(f'O número {numero} não é primo.')