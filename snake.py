import pygame 
import random
from pygame.locals import *
   


def posicaomaca():
    x = random.randint(10,580)
    y = random.randint(10,580)
    return (x //10 * 10, y // 10 * 10)






def colisao(c1, c2):

    return (c1[0]==c2[0] and (c1[1] == c2[1]))

pygame.init()


cima = 0
direita = 1
esquerda = 3
baixo = 2


largura = 600
altura = 600
tamanho_tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Sanke")
tamanho_tela.fill((127,255,212))



cobra = [(200, 200), (210, 200), (220, 200)]


cor_cobra = pygame.Surface((10,10))
cor_cobra.fill((255,255,255))

maca_local = posicaomaca()
maca = pygame.Surface((10,10))
maca.fill((255,0,0))

direcao = esquerda

fps_cobra = pygame.time.Clock()

while True:
    fps_cobra.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    if event.type == pygame.KEYDOWN:
        if event.key == K_UP:
            direcao = cima
        if event.key == K_DOWN:
            direcao = baixo
        if event.key == K_LEFT:
            direcao = esquerda 
        if event.key == K_RIGHT:
            direcao = direita


    
   

    if cobra[0][0] == 600 or cobra[0][1]== 600:
       pygame.quit()

    if cobra[1][0] == 0 or cobra[1][1] == 0:
        pygame.quit()


   


    if colisao(cobra[0], maca_local ):
        maca_local = posicaomaca()
        cobra.append((0,0))
    
    for i in range(len(cobra)-1, 0, -1):
        cobra[i] = (cobra[i - 1][0]), cobra[i - 1][1]
    
    if direcao == cima:
            cobra[0] = (cobra[0][0], cobra[0][1] - 10)

    if direcao == baixo:
            cobra[0] = (cobra[0][0], cobra[0][1] + 10)

    if direcao == direita:
            cobra[0] = (cobra[0][0] +10 , cobra[0][1] )

    if direcao == esquerda:
            cobra[0] = (cobra[0][0] -10 , cobra[0][1] )
    
    
    
    
    tamanho_tela.fill((0,50,0))
    tamanho_tela.blit(maca, maca_local)
    for pos in cobra:
        tamanho_tela.blit(cor_cobra, pos)





    pygame.display.update()