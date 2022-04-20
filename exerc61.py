# REFAÇA O DESAFIO 51.
# LENDO O PRIMEIRO TERMO E A RAZÃO DE UMA PA.
# MOSTRANDO OS 10 PRIMEIROS TERMOS DA PROGRESSÃO USANDO A ESTRUTURA WHILE.
primeiro_termo = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Qual a razão da P.A.? '))
termo = primeiro_termo
contador = 1
while contador <= 10:
    termo += razao
    print(f'{termo} -> ', end ='')
    contador += 1
print('FIM')
