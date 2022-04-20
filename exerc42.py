#  REFAÇA O EXERCÍCIO 35 DOS TRIÂNGULOS, ACRESCENTANDO O RECURSO DE MOSTRAR QUE TIPO DE TRIÂNGULO SERÁ FORMADO:
#   -EQUILÁTERO: TODOS OS LADOS IGUAIS
#   -ISÓSCELES: DOIS LADOS IGUAIS
#   -ESCALENO: TODOS OS LADOS DIFERENTES

print('~' * 40)
print('Analisador de Triângulos')
print('~' * 40)
medida1 = float(input('Digite a primeira medida: '))
medida2 = float(input('Digite a segunda medida: '))
medida3 = float(input('Digite a terceira medida: '))
triangulo = [medida1, medida2, medida3]
maior_lado = max(triangulo)
if maior_lado == medida3:
    resultado = medida1 + medida2 > medida3
    
if maior_lado == medida1:
    resultado = medida2 + medida3 > maior_lado
        
if maior_lado == medida2:
    resultado = medida3 + medida1 > maior_lado

if resultado == True and medida1 == medida2 == medida3:
    print('É um triângulo equilátero!')
elif resultado == True and medida1 == medida2 or medida1 == medida3 or medida2 == medida3:
    print('É um triângulo isósceles!')
elif resultado == True:
    print('É um triângulo escaleno!')

else:
    print('Não é possível formar um triângulo!')

