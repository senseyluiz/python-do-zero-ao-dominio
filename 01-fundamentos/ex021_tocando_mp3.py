# 021
# Faça um programa em python que abre e reproduza o audio de um arquivo MP3
import pygame
pygame.init()
pygame.mixer.init()

# Carrega a música (verifique se o caminho está correto)
try:
    pygame.mixer.music.load('Bella_Cio.mp3')
    pygame.mixer.music.play()
except pygame.error:
    print("Erro: Arquivo não encontrado ou formato incompatível.")

# Loop para manter o programa vivo enquanto a música toca
while pygame.mixer.music.get_busy():
    pygame.event.pump()  # Essencial para processar eventos internos
    pygame.time.Clock().tick(10)

