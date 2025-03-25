import pygame
from models.Ball import Ball
from models.Player import Player
import random

pygame.init()

#window settings
windowWidth, windowHeight = 1280, 720
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("[PILOT] BINGO SIMULATOR") #alteração de ideia: pendulo de newton
clock = pygame.time.Clock()
    
def verifica_colisao(a1, b1, contador):
    if a1.x == b1.x+b1.width:
        a1.inverterX()
        print(contador, "COLIDIU!")
        contador+=1
    if a1.y == b1.y+b1.height:
        a1.inverterY()
        print(contador, "COLIDIU!")
        contador+=1


b1 = Ball(window)
b2 = Ball(window)
p1 = Player(window)
p2 = Player(window)

p2.x = 1870

contador = 0
running = True
player_group = pygame.sprite.Group()
player_group.add(p1)
player_group.add(p2)

ball_group = pygame.sprite.Group()
ball_group.add(b1)
ball_group.add(b2)

while running:
    window.fill((255,255,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    ball_group.draw(window)
    #b1.draw()
    b1.move()
    b1.colisao()

    b2.move()
    b2.colisao()

    player_group.draw(window)
    #p1.draw()
    p1.move()
    p1.colisao()

    p2.move()
    p2.colisao()

    #verifica_colisao(b1,p1,contador)

    print(b1.x, b1.y)

    colidiu = pygame.sprite.spritecollide(b1, player_group, False)
    print(colidiu)
    if colidiu:
        b1.inverterX()
        print("Olá!")


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
