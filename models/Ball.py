import pygame, random

class Ball:
    def __init__(self, window):
        self.window = window
        self.radius = 25
        self.x = random.randint(1,window.get_width()-1)
        self.y = random.randint(1,window.get_height()-1)
        self.velocity_x = random.choice([-5,5])
        self.velocity_y = random.choice([-5,5])
        self.color = (255,0,0)

    def move(self):
        self.y += self.velocity_y
        self.x += self.velocity_x

    def inverterY(self):
        self.velocity_y *= -1
    
    def inverterX(self):
        self.velocity_x *= -1

    def colisao(self):
        if self.y >= self.window.get_height():
            self.inverterY()
        if self.y <= 0:
            self.inverterY()
        if self.x >= self.window.get_width():
            self.inverterX()
        if self.x <= 0:
            self.inverterX()
        

    def draw(self):
        pygame.draw.circle(self.window,self.color,(self.x,self.y),self.radius)
