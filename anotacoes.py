# anotações 
# # Desafio da aula 4 deu problema porque, foi ensinado o comando input, mas, esse comando quando é dado para números, (ex: input ('qual é a sua idade?')), ele não consegue compreender o valor da resposta de forma numérica, e pra isso é necessário utilizar o comando int, (ex: int ( input ('Qual é a sua idade?')), dessa forma, o programa compreende o valor numérico da resposta, e o dado pode ser usado para demais situações. Do contrário, o código quebra.
# n1 = input('Digite um número?')
# n2 = input ('Digite mais um número?')
# s  = n1+n2
# # print ('A soma vale ',s)
# # Nesse exemplo acima, ao invés do print exibir a adição de dois números, ele mostra na verdade a junção dos dois números, portanto o teste falhou.
#  n1= int (input('Digite um número: '))
#  n2= int (input('Digite mais um número: '))
#  s= n1+n2
# print ('A soma vale ',s)
# Como podemos ver, é necessário atribuir ao input a função int, para que seja interpretado a resposta com um valor númerico.
#******TIPOS PRIMITIVOS NO PYTHON - OS 4 MAIS IMPORTANTES SAO:
#  int: números inteiros (valores postivos, negativos ou nulos)
# float: números reais ou números de ponto flutuante (valores com ponto, 4.5, 0.00074, etc)
# bool: valores lógicos ou booleanos (True/False sempre usando a primeira letra maiúscula)
# str: valores caractéres ou strings ('Olá' sentenças, que pode ser números e sempre estarão entre aspas)
# --método da própria string: format {}
# n1= int (input('Digite um número: '))
# n2= int (input('Digite mais um número: '))
# s= n1+n2
# print (f'A soma vale {s}')
# print ('A soma vale {}.'.format(s))
# ---------------
# OPERADORES ARITMÉTICOS: + adição   - subtração    *multiplicação    /divisão   **potência    //divisão inteira    %resto da divisão
# Para calcular o valor de uma equação, é necessário utilizar dois símbolos de igual, pois, quando colocamos um símbolo apenas, o  programa o interpreta como 'recebe' e não como =
# ORDEM DE PRECEDÊNCIA: 1() 2** 3 * / // %  4 + -
