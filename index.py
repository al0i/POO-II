import pygame
from models.Ball import Ball

pygame.init()

#window settings
windowWidth, windowHeight = 1280, 720
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("[PILOT] BINGO SIMULATOR")
clock = pygame.time.Clock()
    
b1 = Ball(window)

running = True
while running:
    window.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    b1.draw()
    
    b1.move()
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
