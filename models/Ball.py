import pygame, random

class Ball(pygame.sprite.Sprite):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.radius = 25
        self.x = random.randint(1,window.get_width()-1)
        self.y = random.randint(1,window.get_height()-1)
        self.velocity_x = -5#random.choice([-5,5])
        self.velocity_y = random.choice([-5,5])
        self.color = (255,0,0)
        self.width = 25
        self.height = 25
        self.image = pygame.Surface((2*self.radius, 2*self.radius))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def move(self):
        self.rect.y += self.velocity_y
        self.rect.x += self.velocity_x

    def inverterY(self):
        self.velocity_y *= -1
    
    def inverterX(self):
        self.velocity_x *= -1

    def colisao(self):
        if self.rect.y >= self.window.get_height() or self.rect.y <= 0:
            self.inverterY()
        if self.rect.x >= self.window.get_width() or self.rect.x <= 0:
            self.inverterX()

    def draw(self):
        pygame.draw.circle(self.window,self.color,(self.x,self.y),self.radius)
