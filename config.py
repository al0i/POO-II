import pygame
from models.Ball import Ball
from models.Player import Player

#Window setting
windowWidth, windowHeight = 1280, 720
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("[PILOT] BEEs") #alteração de ideia: pendulo de newton
clock = pygame.time.Clock()

def display_config():
    pygame.display.flip()
    pygame.display.update()
    clock.tick(20)