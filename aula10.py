tempo = int(input('Quanto tempo tem o seu carro? '))
if tempo <=3:
    print('Carro novo!')

else:
     print('Carro velho!')

print('Carro novo!'if tempo<=3 else 'Carro velho!')
# condição simplificada, mas é mais complicado de entender qual bloco é o verdadeiro e qual é o falso.
print('****FIM****')
nome = str(input('Qual é o seu nome? '))
if nome == 'Filipe' or nome == 'Fil':
    print('É o nome do amor da minha vida!')
else:
    print('Gostei do seu nome!')
print(f'Boa tarde, {nome}!')

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1+nota2)/2
print(f'A sua média ficou {media:.1f}.')
if media >=7:
    print('Parabéns pelo semestre!')
else:
    print('Infelizmente será necessário uma nova prova de recuperação!')
