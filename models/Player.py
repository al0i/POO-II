import pygame

class Player:
    def __init__(self, Paddle, ball_group):
        self.paddle = Paddle
        self.ball_group = ball_group.sprites()
        self.choiced_ball = None

    def update(self):
        self.autoMove()

    def moverY(self,y):
        if y < self.paddle.getCenter() - self.paddle.velocity:
            self.paddle.moveUp()
            return True
        elif y > self.paddle.getCenter() + self.paddle.velocity:
            self.paddle.moveDown()
            return True
        else:
            self.paddle.stop()
            return False

    def showBallsRoute(self):
        for b in self.ball_group:
            if b.isAlive:
                self.calcularRota(b)
    
    def decision(self):
        comming_balls = self.comingBalls()

        if comming_balls:
            mais_proxima = min(comming_balls, key=lambda b: abs(b.getX() - self.paddle.rect.centerx))
            self.setChoicedBall(mais_proxima)
            return mais_proxima
        else:
            self.setChoicedBall(None)
            return None
    
    def updateBallGroup(self, ball_group):
        self.ball_group = ball_group
    
    def closerComingBall(self):
        if self.paddle.n == 1:
            coming_balls = [b for b in self.ball_group if b.velocity_x < 0 and b.getX() > self.paddle.rect.right]
            #for ball in coming_balls:
            #    ball.color = (255,0,255)
            if not coming_balls:
                return None
            closer_ball = min(coming_balls, key=lambda b: b.getX()) #!
            return closer_ball

    def autoMove(self):
        self.decision()  # sempre chama para garantir atualização da bola

        if self.choiced_ball:
            self.moverY(self.calcularRota(self.choiced_ball)[1])
        else:
            self.paddle.stop()

    def calcularRota(self, ball_input):
        ball_vx = ball_input.velocity_x
        ball_vy = ball_input.velocity_y
        
        x2 = ball_input.rect.x + ball_vx
        y2 = ball_input.rect.y + ball_vy
        
        cond = (lambda x2, x: x2 > x) if self.paddle.n == 1 else (lambda x2, x: x2 < x) #!

        while cond(x2, self.paddle.rect.x):
                x2 = x2 + ball_vx
                y2 = y2 + ball_vy
                if y2 <= 0:
                    y2 = 0
                    if ball_vy < 0:
                        ball_vy *= -1
                
                elif y2 >= ball_input.window.get_height():
                    y2 = ball_input.window.get_height()
                    if ball_vy > 0:
                        ball_vy *= -1

                if x2 <= 0:
                    x2 = 0
                    if ball_vx < 0:
                        ball_vx *= -1
                
                elif x2 >= ball_input.window.get_width():
                    x2 = ball_input.window.get_width()
                    if ball_vx > 0:
                        ball_vx *= -1
                
                pygame.draw.circle(ball_input.window,(0,255,0),(x2, y2), 4)#ball_input.radius)

        return (x2, y2)

    def setChoicedBall(self, ball):
        if self.choiced_ball and self.choiced_ball != ball:
            self.choiced_ball.color = (255, 0, 0)
        self.choiced_ball = ball
        if ball:
            ball.color = self.paddle.color
        return True
    
    def comingBalls(self):
        if self.paddle.n == 1:
            return [b for b in self.ball_group if b.isAlive and b.velocity_x < 0 and b.getX() > self.paddle.rect.right]
        elif self.paddle.n == 2:
            return [b for b in self.ball_group if b.isAlive and b.velocity_x > 0 and b.getX() < self.paddle.rect.left]
        else:
            return []

    def method(self, method):
        if method == 'range' and self.comingBalls():
            allRoutes = []
            for ball in self.comingBalls():
                route = self.calcularRota(ball)
                allRoutes.append(route)
                #pygame.draw.circle(self.paddle.window, (255, 0, 255), route, 10)

            radarRange = self.paddle.height
            radar = {}

            for (_, y) in allRoutes:
                radarY = (y // radarRange) * radarRange
                radar[radarY] = radar.get(radarY, 0) + 1

            if radar:
                bestRadarY = max(radar, key=radar.get)
                radarCenter = bestRadarY + radarRange // 2
                self.moverY(radarCenter)
        if method == 'closer':
            self.autoMove()