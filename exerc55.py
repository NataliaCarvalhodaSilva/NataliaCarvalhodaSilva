# FAÇA UM PROGRAMA QUE LEIA O PESO DE CINCO PESSOAS.
# NO FINAL, MOSTRE QUAL FOI O MAIOR E O MENOR PESO LIDOS.
maior_peso = 0
menor_peso = 0
for peso in range (1, 6):
    peso_pessoa = float(input(f'Digite o pesoa da pessoa {peso}: '))
    if peso == 1:
        maior_peso = peso_pessoa
        menor_peso = peso_pessoa
# Nesse caso acima eu tornei a medida inicial, o primeiro peso inserido.
    else:
        if peso_pessoa > maior_peso:
            maior_peso = peso_pessoa
        if peso_pessoa < menor_peso:
            menor_peso = peso_pessoa
print(f'O maior peso lido foi {maior_peso}kg e, o menor peso lido foi {menor_peso}kg.')
