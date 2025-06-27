from config import *

pygame.init()

running = True
while running:
    window.fill((255,255,0)) #YELLOW
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    paddle_group.update()
    ball_group.update()
#    for p in player_group:
#        p.update()
    player1.decision()
    player1.autoMove()
    #player1.showBallsRoute()
    
    vai_morrer = []

    for b in ball_group:
        colided = pygame.sprite.spritecollide(b, paddle_group, False)
        if not b.isAlive:
            vai_morrer.append(b)
        if colided:
            # Detectar a direção do movimento da bola
            if b.velocity_x > 0:  # bola indo para a direita
                b.rect.right = colided[0].rect.left  # encosta a bola no lado esquerdo do paddle
                b.invertX()
                player1.setChoicedBall(None)
            elif b.velocity_x < 0:  # bola indo para a esquerda
                b.rect.left = colided[0].rect.right  # encosta a bola no lado direito do paddle
                b.invertX()
                player1.setChoicedBall(None)
    
    for b in vai_morrer:
        ball_group.remove(b)
        #for bola in ball_group:
        #    bola.aumentaVelocidade()

    display_config()

pygame.quit()
