import pygame, random

class Ball(pygame.sprite.Sprite):
    def __init__(self, window):
        pygame.sprite.Sprite.__init__(self)
        self.window = window
        self.velocity_x = random.choice([-5,5])
        self.velocity_y = random.choice([-5,5])
        self.color = (255,0,0) #RED
        self.radius = 10
        self.image = pygame.Surface((self.radius*2,self.radius*2))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(self.radius, window.get_width() - self.radius), random.randint(self.radius, window.get_height() - self.radius))
        self.image.fill(self.color)
        self.isAlive = True

    def move(self):
        self.rect.y += self.velocity_y
        self.rect.x += self.velocity_x

    def update(self):
        self.move()
        self.screenColision()
        self.draw()
        if self.screenColision() in ["left", "right"]:
            self.isAlive = False

    def aumentaVelocidade(self):
        self.velocity_x *= 1.1
        self.velocity_y *= 1.1
        return True

    def invertY(self):
        self.velocity_y *= -1
    
    def invertX(self):
        self.velocity_x *= -1
        
    def screenColision(self):
        if self.rect.left <= 0:
            self.rect.left = 0
            if self.velocity_x < 0:
                return "left"
        
        elif self.rect.right >= self.window.get_width():
            self.rect.right = self.window.get_width()
            if self.velocity_x > 0:
                return "right"
        
        if self.rect.top <= 0:
            self.rect.top = 0
            if self.velocity_y < 0:
                self.invertY()
                return "top"
        
        elif self.rect.bottom >= self.window.get_height():
            self.rect.bottom = self.window.get_height()
            if self.velocity_y > 0:
                self.invertY()
                return 'bottom'
        
        return False

    def getY(self):
        return self.rect.y
    
    def getX(self):
        return self.rect.x

    def draw(self):
        pygame.draw.circle(self.window, self.color, self.rect.center, self.radius)
