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
        #self.rect = self.image.get_rect(topleft=(random.randint(1,window.get_width()-1), random.randint(1,window.get_height()-1)))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(self.radius, window.get_width() - self.radius), random.randint(self.radius, window.get_height() - self.radius))
        #self.image.set_colorkey((0,255,0))
        self.image.fill(self.color)

    def move(self):
        self.rect.y += self.velocity_y
        self.rect.x += self.velocity_x

    def update(self):
        self.move()
        self.screenColision()
        self.draw()

    def invertY(self):
        self.velocity_y *= -1
    
    def invertX(self):
        self.velocity_x *= -1
        
    def screenColision(self):
        if self.rect.left <= 0:
            self.rect.left = 0
            if self.velocity_x < 0:
                self.invertX()
                return True
        
        elif self.rect.right >= self.window.get_width():
            self.rect.right = self.window.get_width()
            if self.velocity_x > 0:
                self.invertX()
                return True
        
        if self.rect.top <= 0:
            self.rect.top = 0
            if self.velocity_y < 0:
                self.invertY()
                return True
        
        elif self.rect.bottom >= self.window.get_height():
            self.rect.bottom = self.window.get_height()
            if self.velocity_y > 0:
                self.invertY()
                return True
        
        return False

    def getY(self):
        return self.rect.y
    
    def getX(self):
        return self.rect.x

    def draw(self):
        pygame.draw.circle(self.window, self.color, self.rect.center, self.radius)