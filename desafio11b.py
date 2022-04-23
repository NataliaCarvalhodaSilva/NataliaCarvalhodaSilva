# FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS, CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA, SABENDO QUE CADA LITRO DE TINTA, PINTA UMA ÁREA DE 2M2.
largura = float(input('Digite a largura do local: '))
altura = float(input('Digite a altura do local: '))
area = largura * altura
tintas = area / 2
print('A largura do local é {} e a altura {}, portanto sua área é {}. Serão necessárias {} latas tinta para pintura.'.format(largura, altura, area, tintas))
print(f'A largura do local é {largura} e a altura é {altura}, portanto sua área é {area}. Serão necessárias {tintas} latas de tinta para pintura.')
