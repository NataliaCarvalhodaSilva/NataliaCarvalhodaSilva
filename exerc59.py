# CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU NA TELA:
#     [1]SOMA
#     [2]MULTIPLICAR
#     [3]MAIOR
#     [4]NOVOS NÚMEROS
#     [5]SAIR DO PROGRAMA
# SEU PROGRAMA DEVERÁ REALIZAR A OPERAÇÃO SOLICITADA EM CASA CASO.
operador = 0
primeiro_numero_escolhido = int(input('Digite um valor: '))
segundo_numero_escolhido = int(input('Digite um valor: '))
while operador != 5:
    operador = int(input('Escolha uma opção abaixo: \n [1] SOMA \n [2] MULTIPLICAR \n [3] MAIOR NÚMERO  \n [4] NOVOS NÚMEROS \n [5] SAIR DO PROGRAMA \n '))
    if operador == 1:
        resultado = primeiro_numero_escolhido + segundo_numero_escolhido
        print(f'O resultado da operação foi {resultado}.')
    if operador == 2:
        resultado = primeiro_numero_escolhido * segundo_numero_escolhido
        print(f'O resultado da operação foi {resultado}.')
    if operador == 3:
        lista = [primeiro_numero_escolhido, segundo_numero_escolhido]
        resultado = max(lista)
        print(f'O resultado da operação foi {resultado}.') 
    if operador == 4:
        primeiro_numero_escolhido = int(input('Digite um valor: '))
        segundo_numero_escolhido = int(input('Digite um valor: '))
    if operador != 1 and operador != 2 and operador != 3 and operador != 4 and operador != 5:
        print('Opção inválida!')
print( 'VOCÊ SAIU DO PROGRAMA!')
