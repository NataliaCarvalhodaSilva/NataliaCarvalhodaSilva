# ******************************************************************
#            VARIÁVEIS COMPOSTAS - TUPLAS
# ******************************************************************

lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'batata frita')

for comida in lanche: 
    print(f'Eu vou comer {comida}.')
# não precisa da posição em que está 
for comida in range (0, len(lanche)):
    print(f'Eu  vou comer {lanche [comida]}, na posição {comida}.')

for posicao, comida in enumerate(lanche): 
    print(f'Eu vou comer {comida}, na posição {posicao}')
print('Comi pra caramba !')
print(sorted(lanche))

# TUPLAS SÃO IMUTÁVEIS
# para mudar a tupla, não é possível durante ele rodando
# precisa parar o programa, mudar a tupla, e depois rodar o programa
# as variáveis compostas podem começar com: () [] {}
# as tuplas no Pytho novo não precisa dos ()
a = (2,5, 4)
b = (5,8,1,2)
c = a + b
print(c)
print(len(c)) 
# ^quantos caracteres tem a tupla (conta os espaços)
print(c.count(5))
# ^quantas vezes aparece o item
print(c.index(8))
# ^qual a primeira posição em que aparece o item
print(c.index(5, 1))
# ^quis eliminar a contagem da primeira posição em que aparece (0), e começar pelo 1
# del(a) - deleta a tupla de a do sistema

