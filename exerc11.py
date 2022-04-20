#FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS, CALCULE SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA.
#SABENDO QUE CADA LITRO DE TINTA, PINTA UMA ÁREA DE 2 METROS QUADRADOS.
l = float(input('Digite a largura da parede em metros: '))
a = float(input('Digite a altura da parede em metros: '))
ar = l*a
t = ar / 2
print(f'Serão necessárias {t} litros de tinta para pintar a área de {ar:.2f}m2.')
