# DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRÊS RETAS E DIGA AO USUÁRIO SE ELAS PODEM OU NÃO FORMAR UM TRIÂNGULO.

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

if resultado == True:
    print('Pode formar um triângulo!')
else:
    print('Não formará um triângulo!')

if medida1 < medida2 + medida3 and medida2 < medida1 + medida3 and medida3 < medida1 + medida2:
    print(f'As medidas {medida1}, {medida2} e {medida3}, podem formar um triângulo.')
else:
    print(f'As medidas {medida1}, {medida2} e {medida3}, não podem formar um triângulo.')
    

