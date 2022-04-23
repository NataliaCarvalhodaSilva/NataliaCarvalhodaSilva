# PRECISO COMPRAR TINTA DE CABELO. TEM UMA PROMOÇÃO DA TINTA AZUL COM DESCONTO DE 32%. O VALOR DA TINTA NORMAL É R$25,00. CALCULAR O VALOR TOTAL DA COMPRA COM O DESCONTO, DE ACORDO COM O NÚMERO DE TINTAS QUE VOCÊ VAI COMPRAR.
# DESC 32%]
# TINTA 25 REAIS 

# tintas = int(input('Quantas tintas você vai comprar: '))
# total = tintas * 25
# porcentagem = total * 0.32
# vf = total - porcentagem
# print (f'O total da compra foi R${total}, com desconto ficou R${vf}.')

preço = float(input('Digite o valor do produto: '))
porcentagem = float(input('Digite o valor da porcentagem: '))
p = porcentagem / 100
desc = preço * p
total = preço - desc
print(f'O valor final é R${total}.')
