# DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA PA.
# NO FINAL, MOSTRE OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO.
termo = int(input('Digite o termo da P.A.: '))
razao = int(input('Qual a razão da P.A.? '))
# uma progressão aritmética é quando você soma ao termo a razão. então a subtração da razão deve ser igual o número anterior.
termo_final = termo + (11 - 1) * razao
for c in range (termo, termo_final, razao):
   print(c, end='-> ')
print('ACABOU!')