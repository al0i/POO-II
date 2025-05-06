import pygame, random

class Player(pygame.sprite.Sprite):
    def __init__(self, window, n):
        super().__init__()
        self.window = window
        self.width = 10
        self.height = 250
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect(topleft=(50 if n == 1 else window.get_width()-50 if n == 2 else window.get_width()/2, 0))
        self.velocity_y = 5
        self.velocity_x = 5
        self.color = (0,0,255)
        self.pontos = 0

    def update(self):
        self.move()
        self.colisao()

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

#mesma coisa que nada
    def draw(self):
        pygame.draw.rect(self.window,self.color,pygame.Rect(self.rect.x, self.rect.y, self.width, self.height))
