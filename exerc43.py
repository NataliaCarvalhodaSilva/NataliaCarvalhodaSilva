#  DESENVOLVA UMA LÓGICA QUE LEIA O PESO E A ALTURA DE UMA PESSOA, CALCULE SEU IMC E MOSTRE SEU STATUS, DE ACORDO COM A TABELA ABAIXO:
#    -ABAIXO DE 18.5: ABAIXO DO PESO
#    -ENTRE 18.5 E 25: PESO IDEAL
#    -DE 25 ATÉ 30: SOBREPESO
#    -DE 30 ATÉ 40: OBESIDADE
#    -ACIMA DE 40: OBESIDADE MÓRBIDA
print('-' * 40)
altura = float(input('Qual é a sua altura: '))
peso = float(input('Qual é o seu peso? '))
imc = peso / (altura ** 2)
print('-' * 40)

if imc < 18.5:
    print(f'IMC {imc:.2f}: ABAIXO DO PESO.')

elif imc >= 18.5 and imc < 25:
    print(f'IMC {imc:.2f}: PESO IDEAL.')

elif imc >= 25 and imc < 30:
    print(f'IMC {imc:.2f}: SOBREPESO.')

elif imc >= 30 <= 40:
    print(f'IMC {imc:.2f}: OBESIDADE.')

else:
    print(f'IMC {imc:.2f}: OBESIDADE MÓRBIDA.')

print('-' * 40)
print('Cuide-se!')
