#  CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE SUA MÉDIA, MOSTRANDO UMA MENSAGEM NO FINAL, DE ACORDO COM A MÉDIA ATINGIDA:
#   -MÉDIA ABAIXO DE 5.0: REPROVADO
#   -MÉDIA ENTRE 5.0 E 6.9: RECUPERAÇÃO
#   -MÉDIA 7.0 OU SUPERIOR: APROVADO
from time import sleep
print('-' * 40)
nota_1 = float(input('Insira a primeira nota do semestre: '))
nota_2 = float(input('Insira a segunda nota do semestre: '))
print('Estamos calculando...')
print('-' * 40)
sleep(5)
media_semestral = (nota_1 + nota_2) / 2
if media_semestral < 5.0:
    print(f'Você foi REPROVADO! Sua média foi {media_semestral}.')
elif media_semestral >= 5.0 and media_semestral < 7:
    print(f'Você está de RECUPERAÇÃO! Sua média ficou {media_semestral}.')
else:
    print(f'Você foi APROVADO! Sua média ficou {media_semestral}.')
    # nesta última opção pode ser usado o elif pra ficar mais claro.
print('Até o próximo semestre!')
