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
        if self.rect.y*1.05 >= self.window.get_height() or self.rect.y*1.05 <= 0:
            self.invertY()
            return True
        if self.rect.x*1.05 >= self.window.get_width() or self.rect.x*1.05 <= 0:
            self.invertX()
            return True
        return False

    def getY(self):
        return self.rect.y

    def draw(self):
        pygame.draw.circle(self.window,self.color,(self.rect.x,self.rect.y),self.radius)
