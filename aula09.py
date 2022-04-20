# MANIPULAÇÃO DE STRINGS --- CADEIAS DE CARACTÉRES --- CADEIAS DE TEXTO

# ***Fatiamento***
frase = 'Curso em Vídeo Python'
print(frase[:21])
# ***Análise***
print(len(frase))
print(frase.count('o',0, 13))
print(frase.find('android'))
# ***Transformação***
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
# quando se coloca parênteses vazio, significa que você está chamando uma função.
print(frase.capitalize())
print(frase.title())
novafrase = '   Aprenda Python  '
# Funcionalidade específica para retirar espaços desnecessários
print(novafrase.strip())
print(novafrase.rstrip())
# a string acima elimina o espaço da esquerda da frase, mas mantém os da direita.
print(novafrase.lstrip())
# ***Divisão***
print(frase.split())
# divide uma string em uma lista
# ***Junção***
print('-'.join(frase))
# Utiliza-se em frases longas, ou menos, 3 aspas no inicio da string, e 3 no final, na função print.
print('curso' in frase)