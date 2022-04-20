# MELHORE O DESAFIO 61, PERGUNTANDO PARA O USUÁRIO SE ELE QUER MOSTRAR MAIS ALGUNS TERMOS.
# O PROGRAMA ENCERRA QUANDO ELE DISSER QUE QUER MOSTRAR 0 TERMOS.
primeiro_termo = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Qual a razão da P.A.? '))
termo = primeiro_termo
contador = 1
resposta = 10
total = 0
while resposta != 0:
    total = total + resposta
    while contador <= total:
        termo += razao
        print(f'{termo} -> ', end ='')
        contador += 1
    print('PAUSA')
    resposta = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Foram mostrados {total} números.')
print('FIM')
