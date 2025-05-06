from config import *

pygame.init()

balls = 20
ball_group = pygame.sprite.Group()
for i in range(balls):
    i = Ball(window)
    ball_group.add(i)

p1 = Player(window, 1)
p2 = Player(window, 2)
p3 = Player(window, 3)
p3.velocity_y = 0
p3.color = (255,0,0)
p3.height = 600
p3.width = 60
p3.image = pygame.Surface((p3.width, p3.height))
p3.rect.y = (window.get_height()/2)-p3.height/2
player_group = pygame.sprite.Group()
player_group.add(p1)
player_group.add(p2)
player_group.add(p3)

running = True
while running:
    window.fill((255,255,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player_group.update()
    player_group.draw(window)
    

    ball_group.draw(window)
    ball_group.update()


    for b in ball_group:
        #b.update()
        #window.blit(b.image,b.rect)
        colided = pygame.sprite.spritecollide(b, player_group, False)
        if colided:
            b.invertX()
            ball_group.remove(b)
        colided = False
        #colided_between = pygame.sprite.spritecollide(b, b, False)
        #if colided_between:
        #    b.invertX()
        #    b.invertY()

    display_config()

pygame.quit()
