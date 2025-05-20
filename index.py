from config import *

pygame.init()

balls = 0
ball_group = pygame.sprite.Group()
for i in range(balls):
    i = Ball(window)
    ball_group.add(i)

b1 = Ball(window)
ball_group.add(b1)

p1 = Paddle(window, 1)
p2 = Paddle(window, 2)
paddle_group = pygame.sprite.Group()
paddle_group.add(p1)
paddle_group.add(p2)

j1 = Player(p1, b1)

running = True
while running:
    window.fill((255,255,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    paddle_group.update()
    paddle_group.draw(window)
    

    ball_group.draw(window)
    ball_group.update()

    for b in ball_group:
        colided = pygame.sprite.spritecollide(b, paddle_group, False)
        if colided:
            b.invertX()
        colided = False

    display_config()

pygame.quit()
