# FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NÚMEROS ÍMPARES QUE SÃO MÚLTIPLOS DE TRÊS.
# E QUE SE ENCONTRAM NO INTERVALO DE 1 ATÉ 500.
soma_dos_multiplos = 0
for contagem in range (1, 501):
    if contagem % 2 ==1 and contagem % 3 == 0:
        soma_dos_multiplos = contagem + soma_dos_multiplos
        print(contagem, end=' ')
print(soma_dos_multiplos, end=' ')
# é necessário um valor de referência para o início do loop.
soma = 0
cont = 0
for contagem in range (1, 501, 2):
    if contagem % 3 == 0:
        soma = soma + contagem
        cont = cont + 1 
        # esse cont está contando quantos números ímpares e divisíveis por 3 estão sendo contados.
        print(contagem, end=' ')
print(f'A soma de todos os {cont} valores é {soma}.')
