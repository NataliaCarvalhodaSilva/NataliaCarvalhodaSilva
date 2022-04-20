# CRIE UM PROGRAMA QUE MOSTRE NA TELA TODOS OS NÚMEROS PARES QUE ESTÃO NO INTERVALO ENTRE 1 E 50.
for contagem in range (1, 50+1):
    if contagem % 2 == 0:
        print(contagem, end=' ')
# ou
for contagem in range (2, 51, 2):
    print(contagem, end=' ')
print('Acabou!')
# essa segunda forma é pra poupar o processador de duas casas que serão contadas desnecessariamente.
