# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
n = input('Digite algo: ')
print ('is identifier: ', n.isidentifier ())
print ('is alnun: ', n.isalnum ())
print ('is alpha: ', n.isalpha())
print ('is ascii: ', n.isascii ())
print ('is decimal: ', n.isdecimal ())
print ('is digit: ', n.isdigit ())
print ('is lower: ', n.islower ())
print ('is numeric: ', n.isnumeric ())
print ('is printable: ', n.isprintable ())
print ('is space: ', n.isspace ())
print ('is title: ', n.istitle ())
print ('is upper: ', n.isupper ())
print (bool(n))
print (str(n))