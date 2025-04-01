
import pygame #

running = True #
window = pygame.display.set_mode((800,600))#
pygame.display.set_caption('Race car')#

############################################
class car(pygame.sprite.Sprite):
    def __init__(self,location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('racecar.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = location

car1 = car([370,430])
car2 = car([100,430])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((0, 0, 0))
    window.blit(car1.image,car1.rect)
    window.blit(car2.image,car2.rect)
    pygame.display.update()