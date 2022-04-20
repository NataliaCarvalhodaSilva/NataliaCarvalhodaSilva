# FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE:  
# *quantas vezes aparece a letra "A"
# *em que posição ela aparece a primeira vez
# * em que posição ela aparece a última vez
frase = str(input('Escreva uma frase: ').strip())
frase = frase.lower()
letra = frase.count('a')
primeira = frase.index('a')
ultimo = frase.rindex('a')
print(f'A letra a aparece {letra} vezes, pela pimeira vez aparece na posição {primeira} e por último na posição {ultimo}.')
