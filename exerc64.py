# CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO.
# O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR 999, QUE É A CONDIÇÃO DE PARADA.
# NO FINAL, MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS E QUAL FOI A SOMA ENTRE ELES.
# DESCONSIDERANDO O FLAG.
numero_inserido = 0
contagem = 0
soma = 0
while not numero_inserido == 999:
    numero_inserido = int(input('Digite um número: [999] é a condição para parar!'))
    contagem += 1
    soma = soma + numero_inserido
    if numero_inserido == 999:
        contagem -= 1
        soma = soma - 999
print(f'A quantidade de números inseridos foi {contagem}, e a soma deles é igual a {soma}.')
