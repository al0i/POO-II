import pygame

class Ball:
    def __init__(self, window):
        self.x = 1280/2
        self.y = 720/2
        self.velocity_x = 5
        self.velocity_y = 5
        self.radius = 15
        self.color = (255,0,0) #branco
        self.window = window

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

    def draw(self):
        pygame.draw.circle(self.window,self.color,(self.x,self.y),self.radius)
