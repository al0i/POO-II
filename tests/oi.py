import pygame

running = True
window = pygame.display.set_mode((800,600))
pygame.display.set_caption('Race car')
clock = pygame.time.Clock()


class Car(pygame.sprite.Sprite):
    def __init__(self,location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('/home/ifc/al0i/POO-II/tests/racecar.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.image = self.mask.to_surface()

    def move(self):
        self.rect.y += 1

car1 = Car([370,430])
car2 = Car([100,430])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.blit(car1.image,car1.rect)
    window.blit(car2.image,car2.rect)
    pygame.display.update()

    print(car1.image)
    print(car1.image.get_rect())
    print(pygame.mask.from_surface(car1.image))

    if car1.mask.overlap(car2.mask, (car1.rect.x,car1.rect.y)):
        print('!')
        window.fill((255,0,0))
    else:
        window.fill((0, 0, 0))
    print(car1.mask.overlap(car2.mask, (car1.rect.x,car1.rect.y)))


    car1.move()
    clock.tick(30)