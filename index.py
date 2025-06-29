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
            paddle = colided[0]
            
            # Cálculo da diferença de impacto vertical
            impact_point = b.rect.centery - paddle.rect.centery
            normalized = impact_point / (paddle.height / 2)  # -1 (topo) a +1 (base)
            normalized = max(-1, min(normalized, 1))  # Garantir que está no intervalo

            # Define o ângulo máximo (em radianos)
            max_angle = math.radians(70)
            angle = normalized * max_angle

            # Magnitude da velocidade da bola
            speed = (b.velocity_x**2 + b.velocity_y**2) ** 0.5

            # Direção depende de qual paddle colidiu (esquerda ou direita)
            if b.velocity_x > 0:  # bola veio da esquerda → paddle da direita
                new_angle = angle
                b.velocity_x = -speed * math.cos(new_angle)
                b.velocity_y = speed * math.sin(new_angle)
                b.rect.right = paddle.rect.left
            else:  # bola veio da direita → paddle da esquerda
                new_angle = angle
                b.velocity_x = speed * math.cos(new_angle)
                b.velocity_y = speed * math.sin(new_angle)
                b.rect.left = paddle.rect.right

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
