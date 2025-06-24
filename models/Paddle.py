import pygame, random

class Paddle(pygame.sprite.Sprite):
    def __init__(self, window, n):
        super().__init__()
        self.window = window
        self.n = n
        self.width = 10
        self.height = 250
        self.image = pygame.Surface((self.width, self.height))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(50 if n == 1 else window.get_width()-60 if n == 2 else window.get_width()/2, (window.get_height()/2)-(self.height/2)))
        self.velocity = 5
        self.way = 1
        self.color = (0,0,255)
        self.pontos = 0

    def update(self):
        self.move()
        self.screenColision()

    def move(self):
        self.rect.y += self.velocity*self.way
        if self.screenColision():
            self.invertWay()

    def moveUp(self):
        self.way = -1
        if self.screenColision():
            return False
        self.rect.y += self.velocity*self.way
        return True

    def moveDown(self):
        self.way = 1
        if self.screenColision():
            return False
        self.rect.y += self.velocity*self.way
        return True

    def stop(self):
        self.way = 0

    def invertWay(self):
        if self.way == 0:
            return False
        else:
            self.way *= -1
            return True

    def screenColision(self):
        if (self.rect.bottom >= self.window.get_height()) and (self.way == 1):
            return True
        elif (self.rect.top <= 0) and (self.way == -1):
            return True
        return False
        
    def getCenter(self):
        return int(self.rect.y+(self.height/2))

#mesma coisa que nada
    def draw(self):
        pygame.draw.rect(self.window,self.color,pygame.Rect(self.rect.x, self.rect.y, self.width, self.height))
