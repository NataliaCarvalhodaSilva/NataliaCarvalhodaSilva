# FAÇA UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA UM ARQUIVO MP3.
import pygame
import time
pygame.init()
# iniciei o pygame
pygame.mixer.music.load('/home/nati/cursoemvideo.py/02-champagneproblem.mp3')
pygame.mixer.music.play()
pygame.event.wait()
time.sleep(300)
# EXISTEM VÁRIAS BIBLIOTECAS PARA MÚSICAS, FOI UTILIZADA A QUE UTILIZAM PARA JOGOS, porém o comando wait não funcionou.
