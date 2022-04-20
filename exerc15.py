#ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDOS POR UM CARRO ALUGADO E A QUANTIDADE DE DIAS PELOS QUAIS ELE FOI ALUGADO. 
#CALCULE O PREÇO A PAGAR, SABENDO QUE O CARRO CUSTA R$60 POR DIA E R$0,15 POR KM RODADO.
km = float(input('Informe o Km rodado: '))
d = int(input('Digite a quantidade de dias que o carro permaneceu alugado: '))
p = (km * 0.15) + (d * 60)
print(f'O valor total a pagar é R${p:.2f}')