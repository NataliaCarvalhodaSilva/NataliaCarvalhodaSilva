# FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA, MAS SÓ ACEITE OS VALORES 'M' OU 'F'.
# CASO ESTEJA ERRADO, PEÇA A DIGITAÇÃO NOVAMENTE ATÉ TER UM VALOR CORRETO.
genero_valido = False
while genero_valido == False:
    sexo_inserido = str(input('Pertence a qual sexo? [ F / M ]')).upper().strip()[0]
# [0] para pegar a primeira letra, é um fatiamento
    if sexo_inserido == 'F' or sexo_inserido == 'M':
        genero_valido = True
    else:
        print('Resposta inválida!')
print(f'Resposta {sexo_inserido} gravada com sucesso!')
