import pygame
from random import randint


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Ajuste de tela
controle_de_tela = (0,0)
reinicia_posicao = 800
sair_da_tela = 950
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Controle de cores
branco = (255, 255, 255)
preto = (0, 0, 0)
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#CONTADORES
contador_sol = 0
contador_lua = 0
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#PAUSA
pausado = pygame.image.load('Menu/pause.png')
pausado = pygame.transform.scale(pausado, (800, 600))
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#VELOCIDADE ATUAL
velocidade_atual_sol = 6
velocidade_atual_lua = 6
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#CRONOMETROS
timer = 120
espera = 0
pausa = False
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#sorteio
sorteio_x_arco_iris = randint(800, 1300)
sorteio_x_estrela = randint(800, 1300)
sorteio_y_sol = randint(1, 230)
sorteio_y_lua = randint(310, 530)
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Controle das músicas
def musica():
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.load('Sons/Top Gear Music.mp3')
    pygame.mixer.music.play(-1)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Controle encerramento da partida
def stop_game():
    global velocidade_jogo_sol, velocidade_jogo_lua
    velocidade_jogo_sol = 0
    velocidade_jogo_lua = 0
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def cronometro():
    global timer, espera, pausa
    if pausa == False:
        if timer > 0:
            if espera < 30:
                espera += 1
            else:
                timer -= 1
                espera = 0
    else:
        pass
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------#

