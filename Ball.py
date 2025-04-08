import pygame, random

class Ball(pygame.sprite.Sprite):
    def __init__(self, window):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('bee.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(40, 40))
        self.rect = self.image.get_rect()
        self.rect.left = random.randint(1,window.get_width()-1)
        self.rect.top = random.randint(1,window.get_height()-1)
        self.window = window
        self.velocity_x = random.choice([-5,10])
        self.velocity_y = random.choice([-5,10])
        self.image = self.image = pygame.transform.flip(self.image, 0, 0) if self.velocity_x > 0 else pygame.transform.flip(self.image, 1, 0)
        self.color = (255,0,0)
        self.rect = self.image.get_rect(topleft=(random.randint(1,window.get_width()-1), random.randint(1,window.get_height()-1)))

    def move(self):
        self.rect.y += self.velocity_y
        self.rect.x += self.velocity_x

    def update(self):
        self.move()
        self.colisao()


    def invertY(self):
        self.velocity_y *= -1
    
    def invertX(self):
        self.velocity_x *= -1
        if self.velocity_x > 0:
            self.image = pygame.transform.flip(self.image, 1, 0)
        else:
            self.image = pygame.transform.flip(self.image, 0, 0)

    def colisao(self):
        if self.rect.y >= self.window.get_height() or self.rect.y <= 0:
            self.invertY()
        if self.rect.x >= self.window.get_width():
            self.invertX()

    def draw(self):
        pygame.draw.circle(self.window,self.color,(self.rect.x,self.rect.y),self.radius)
