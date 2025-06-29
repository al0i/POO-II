from config import *

pygame.init()
font = pygame.font.Font(None, 60)

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
    
    player1.method('closer')
    player2.method('closer')
    
    player1.updateBallGroup(ball_group)
    player2.updateBallGroup(ball_group)

    vai_morrer = []

    for b in ball_group:
        colided = pygame.sprite.spritecollide(b, paddle_group, False)
        if b.screenColision() == "left":
            paddle2.pontos += 1
        elif b.screenColision() == "right":
            paddle1.pontos += 1
        if not b.isAlive:
            vai_morrer.append(b)
        
        if colided:
            if b.velocity_x > 0:
                b.rect.right = colided[0].rect.left
                b.invertX()
                player1.setChoicedBall(None)
                player2.setChoicedBall(None)
            elif b.velocity_x < 0:
                b.rect.left = colided[0].rect.right
                b.invertX()
                player1.setChoicedBall(None)
                player2.setChoicedBall(None)
    
    for b in vai_morrer:
        ball_group.remove(b)
        #for bola in ball_group:
        #    bola.aumentaVelocidade()

    text2_surface = font.render(str(paddle2.pontos), True, paddle2.color)
    text2_rect = text2_surface.get_rect()
    text2_rect.topright = (window.get_width(), 0)
    window.blit(font.render(str(paddle1.pontos), True, (0,0,0)),font.render(str(paddle1.pontos), True, (0,0,0)).get_rect())
    window.blit(text2_surface, text2_rect)
    
    addBall()

    display_config()

pygame.quit()
