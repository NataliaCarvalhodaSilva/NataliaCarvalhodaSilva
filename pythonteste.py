# ******AULA 06 
# ~~~~Para ambos exercícios, utilizei número 5 como exemplo (n inteiro int)
# n1= input('Digite um valor :')
# print(type(n1))
# Esperamos que ele reconheça o número digitado com inteiros, porém, como não existe o comando int, ele entende como string *str*.
# n1 = int(input('Digite um valor: '))
# print(type(n1))
# Agora com o comando int, ele interpreta o resulta como um número inteiro
n1 =  int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1+n2
# print('A soma entre {} e {}, é igual a {}'.format (n1, n2, s))
print(f'A soma entre {n1} e {n2} vale {s}')