# FAÇA UM PROGRAMA QUE LEIA UM ÂNGULO QUALQUER E MOSTRE NA TELA O VALOR DO SENO, COSSENO E TANGENTE DESSE ÂNGULO.
import math
ang = float(input('Digite um ângulo: '))
rad = math.radians(ang)
seno = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print(f'O ângulo {ang} possui valor de seno {seno:.1f}, cosseno {cos:.1f} e tangente {tan:.2f}.')
