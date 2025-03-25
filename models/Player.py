import pygame, random

class Player(pygame.sprite.Sprite):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.width = 10
        self.height = 300
        self.x = 50
        self.y = 300#(self.window.get_height()/2)-(self.height/2)
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.velocity_y = 5
        self.velocity_x = 5
        self.color = (255,255,255)

    def move(self):
        self.rect.y += self.velocity_y

    def inverterY(self):
        self.velocity_y *= -1
    
    def inverterX(self):
        self.velocity_x *= -1

    def colisao(self):
        if self.rect.y+self.height >= self.window.get_height() or self.rect.y <= 0:
            self.inverterY()
        if self.rect.x >= self.window.get_width() or self.rect.x <= 0:
            self.inverterX()

    def draw(self):
        pygame.draw.rect(self.window,self.color,(self.x,self.y,self.width,self.height))
