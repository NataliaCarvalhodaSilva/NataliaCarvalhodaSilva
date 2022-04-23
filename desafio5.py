# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA O SEU SUCESSOR E O SEU ANTECESSOR.
n = int(input('Digite um número: '))
s = n + 1 
a = n - 1
print (f'O antecessor do número {n} é ', (n-1),'e seu sucessor é ', (n+1))
print ('O antecessor do número {} é {}, e o seu sucessor é {}'.format(n, a, s))
print (f'O antecessor do número {n} é {a}, e seu sucessor é {s}')
print ('Analisando o número {}, seu antecessor é {} e seu sucessor é {}.'.format(n, (n-1), (n+1)))
print (f'Analisando o número {n}, seu antecessor é {n-1} e seu sucessor é {n+1}.')
# Nas duas últimas opções não criamos variável para sucessor e antecessor, porque não está sendo feito nada com esses dados, e quanto menos variáveis, menos memória utilizamos.
