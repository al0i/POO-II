import pygame
from models.Ball import Ball
from models.Paddle import Paddle
from models.Player import Player

#Window setting
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("[V1] PONG!")
clock = pygame.time.Clock()

def display_config():
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)

balls = 10
ball_group = pygame.sprite.Group()
for b in range(balls):
    b = Ball(window)
    ball_group.add(b)

paddle_group = pygame.sprite.Group()
paddle1 = Paddle(window, 1)
paddle_group.add(paddle1)
paddle2 = Paddle(window, 2)
paddle_group.add(paddle2)

player1 = Player(paddle1, ball_group)
player2 = Player(paddle2, ball_group)
player_group = [player1, player2]

def addBall():
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_UP]:
        b = Ball(window)
        ball_group.add(b)