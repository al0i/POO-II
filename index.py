import pygame
from models.Ball import Ball
from models.Circle import Circle
import random

pygame.init()

#window settings
windowWidth, windowHeight = 1280, 720
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("[PILOT] BINGO SIMULATOR")
clock = pygame.time.Clock()
    
b1 = Ball(window)
c1 = Circle(window)
contador = 0
running = True
while running:
    window.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    b1.draw()
    b1.move()
    b1.colisao()
    
    c1.draw()


    contador+=1
    if b1.x > c1.x+c1.radius or b1.x<c1.x+c1.radius:
        print(contador,"colidiu!")


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
