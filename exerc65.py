# CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO.
# NO FINAL DA EXECUÇÃO, MOSTRE A MÉDIA ENTRE TODOS OS VALORES E QUAL FOI O MAIOR E O MENOR VALORES LIDOS.
# O PROGRAMA DEVE PERGUNTAR AO USUÁRIO SE ELE QUER OU NÃO CONTINUAR A DIGITAR VALORES.
soma = 0
tentativas = 0
resposta = 'S'
lista = []
while resposta == 'S':
    numero = int(input('Digite um valor: '))
    tentativas += 1
    soma = soma + numero
    resposta = str(input('Você deseja continuar? [S/N] ')).upper().strip()[0]
    lista.append(numero)
    while resposta != 'S' and resposta != 'N':
        print('Resposta inválida!')
        resposta = str(input('Você deseja continuar? [S/N] ')).upper()
maior_valor = max(lista)
menor_valor = min(lista)
media = soma / tentativas
print(f'A média dos valores digitados é {media}, e o maior valor é {maior_valor} e o menor valor é {menor_valor}.')
