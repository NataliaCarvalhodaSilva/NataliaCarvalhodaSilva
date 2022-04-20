# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMEÇA OU NÃO COM O NOME "SANTO".
cidade = str(input('Qual o nome da sua cidade? ')).strip()
cidade = cidade.title()
print('Você nasceu em uma cidade que nasceu com a palavra Santo:')
print(cidade.startswith('Santo'))
