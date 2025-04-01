import pygame
from Ball import Ball
from models.Player import Player
import random

pygame.init()

#window settings
windowWidth, windowHeight = 1280, 720
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("[PILOT] BEEs") #alteração de ideia: pendulo de newton
clock = pygame.time.Clock()


#number of blls
balls = 20
ball_group = pygame.sprite.Group()
for i in range(balls):
    i = Ball(window)
    ball_group.add(i)

#Grupo de jogadores
p1 = Player(window)
player_group = pygame.sprite.Group()
player_group.add(p1)


running = True
while running:
    window.fill((255,255,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    p1.move()
    p1.colisao()
    p1.draw()


    #ball_group.draw(window)
    ball_group.update()    
    
    
    for b in ball_group:
        window.blit(b.image,b.rect)
        colided = pygame.sprite.spritecollide(b, player_group, False)
        if colided:
            b.invertX()

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
