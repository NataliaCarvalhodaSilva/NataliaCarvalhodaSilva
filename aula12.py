# ESTRUTURAS DE CONTROLE
# Condições Aninhadas :' colocando uma coisa dentro da outra '
# Na estrutura condicional só temos duas opções:
#           * se é verdadeiro
#           * se é falso
#     dentro da condição: tenho outra condição [condição aninhada]
#    If   Elif    Else   *Sempre tem IF, nem sempre tem ELIF e ELSE
#                        *Se tiver ELIF, pode mesmo assim NÃO ter ELSE
#     Dentro de IF pode usar quantos ELIF forem necessários, mas ELSE, só pode uma ou nenhuma vez.
# ************************************************************************************************
nome = str(input('Qual é o seu nome? ')).strip().title()
if nome == 'Natalia':
    print('Que nome bonito!')
elif nome == 'Maria' or nome == 'Joao' or nome == 'Jose':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Que nome meigo!')
else:
    print('Seu nome é bem normal!')
print(f'Tenha um bom dia, {nome}!')
#     essa é uma estrutura aninhada ******
