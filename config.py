import pygame
from models.Ball import Ball
from models.Paddle import Paddle
from models.Player import Player

#Window setting
windowWidth, windowHeight = 1280, 720
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("[V1] PONG!")
clock = pygame.time.Clock()

def display_config():
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)