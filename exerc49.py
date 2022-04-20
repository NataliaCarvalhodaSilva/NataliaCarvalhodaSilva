# REFAÇA O DESAFIO 009, MOSTRANDO A TABUADA DE UM NÚMERO QUE O USUÁRIO ESCOLHER.
# SÓ QUE AGORA UTILIZANDO O LAÇO FOR.
numero_escolhido = int(input('Digite um número pra ver sua tabuada: '))
for tabuada in range (1, 11):
    print( numero_escolhido, 'x', tabuada, '=', numero_escolhido*tabuada)
# listo os números os quais o número escolhido será multiplicado.
