#  ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E PEÇA PARA O USUÁRIO ESCOLHER QUAL SERÁ A BASE DE CONVERSÃO:
#    *1 PARA BINÁRIO
#    *2 PARA OCTAL
#    *3 PARA HEXADECIMAL
numero_escolhido = int(input('Digite um número inteiro: '))

base_de_conversao = input('''Você deseja converter seu número para: 
1 binario 
2 octal 
3 hexadecimal? ''')

binario = '1'
octal = '2'
hexadecimal = '3'

if base_de_conversao == binario or base_de_conversao == 'binario':
    resultado = bin(numero_escolhido)
    print(f'O número {numero_escolhido} convertido em binário é: {resultado}.')
elif base_de_conversao == octal or base_de_conversao == 'octal':
    resultado = oct(numero_escolhido)
    print(f'O número {numero_escolhido} convertido em octal é: {resultado[2:]}.')
    # coloque no format do resultado 2: para formatar o resultado sem aparecer os dois primeiros números, que são referentes ao formato de conversão. 
    # posso fazer isso nos outros se eu quiser.

elif base_de_conversao == hexadecimal or base_de_conversao == 'hexadecimal':
    resultado = hex(numero_escolhido)
    print(f'O número {numero_escolhido} convertido para hexadecimal é: {resultado}.')

else:
    print('Opção inválida!')

print('Muito doido né?')
