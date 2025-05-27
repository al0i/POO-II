import pygame, random

class Ball(pygame.sprite.Sprite):
    def __init__(self, window):
        pygame.sprite.Sprite.__init__(self)
        self.window = window
        self.velocity_x = random.choice([-5,5])
        self.velocity_y = random.choice([-5,5])
        self.color = (255,0,0)
        self.radius = 10
        self.image = pygame.Surface((20,20))
        self.mask = pygame.mask.from_surface(self.image)
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

    def colisao(self):
        if self.rect.top <= 0:
            self.invertY()
        if self.rect.bottom >= self.window.get_height():
            self.invertY()
        if self.rect.left <= 0:
            self.invertX()
        if self.rect.right >= self.window.get_width():
            self.invertX()

    def getY(self):
        return self.rect.y

    def draw(self):
        pygame.draw.circle(self.window,self.color,(self.rect.x,self.rect.y),self.radius)
