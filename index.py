from config import *

pygame.init()

balls = 0
ball_group = pygame.sprite.Group()
for i in range(balls):
    i = Ball(window)
    ball_group.add(i)

b1 = Ball(window)
ball_group.add(b1)

b2 = Ball(window)
ball_group.add(b2)

print(ball_group.sprites()[0])

p1 = Paddle(window, 1)
p2 = Paddle(window, 2)
paddle_group = pygame.sprite.Group()
paddle_group.add(p1)
paddle_group.add(p2)

j1 = Player(p1, ball_group)
#j2 = Player(p2, ball_group)

running = True
while running:
    window.fill((255,255,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    paddle_group.draw(window)
    ball_group.update()

    for b in ball_group:
        colided = pygame.sprite.spritecollide(b, paddle_group, False)
        if colided:
            # Detectar a direção do movimento da bola
            if b.velocity_x > 0:  # bola indo para a direita
                b.rect.right = colided[0].rect.left  # encosta a bola no lado esquerdo do paddle
                b.invertX()
            elif b.velocity_x < 0:  # bola indo para a esquerda
                b.rect.left = colided[0].rect.right  # encosta a bola no lado direito do paddle
                b.invertX()

    j1.autoMove()
    #j2.autoMove()
    p2.update()

    if b1.screenColision() == 'left':
        p2.pontos += 1
        print("P1: ", p1.pontos," - P2: ",p2.pontos)
    elif b1.screenColision() == 'right':
        p1.pontos += 1
        print("P1: ", p1.pontos," - P2: ",p2.pontos)

    display_config()

pygame.quit()
