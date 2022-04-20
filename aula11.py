# ANSI
# escape sequence 
# \033[style;text;backm]
# \033[0;33;44m
# STYLE 0 none   1 negrito   4  sublinhado    7 negativo 
# TEXT 30 - 37
# BACK 40 - 47
# teste fundo vermelho e letra em branco
# \033[0;30;41m 
# azul o fundo, letra amarela e sublinhado
# \033[4;33;44m
# # fundo amarelo, letra em roxo e negrito
# \033[1;35;43m
# # fundo verde e branco na letra
# \033[0;30;42m
# # letra branca e fundo preto
# \033[m
# # fundo branco e letra preta
# \033[7;30m

a = 3
b = 5
print(f'Os valores de a e b são: \033[1;36m{a}\033[m e \033[1;35m{b}\033[m.')

nome = 'Natália'
rosa = {'\033[35m'}

print(f'Olá! Muito prazer em te conhecer {'rosa', nome}

