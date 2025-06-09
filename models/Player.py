import pygame

class Player:
    def __init__(self, Paddle, Ball):
        self.paddle = Paddle
        self.ball = Ball
        self.color = (0,255,0)
        #self.rect = pygame.Surface((100, 100)).get_rect(topleft=(self.ball.rect.x,self.ball.rect.y))

    def verifyBallY(self):
        return self.ball.getY()

    def moveUp(self):
        self.paddle.moveUp()

    def autoMove(self):
        if self.paddle.n == 1:
            if self.ball.velocity_x < 0:
                if self.paddle.getCenter() < self.calcularRota()[1]:
                    self.paddle.moveDown()
                elif self.paddle.getCenter() > self.calcularRota()[1]:
                    self.paddle.moveUp()
                else:
                    self.paddle.stop()
        
        elif self.paddle.n == 2:
            if self.ball.velocity_x > 0:
                if self.paddle.getCenter() < self.calcularRota()[1]:
                    self.paddle.moveDown()
                elif self.paddle.getCenter() > self.calcularRota()[1]:
                    self.paddle.moveUp()
                else:
                    self.paddle.stop()

    def calcularRota(self):
        #pygame.draw.circle(self.ball.window, (0,255,0), self.ball.rect.center, 50, 3)
        x2 = self.ball.rect.x + self.ball.velocity_x
        y2 = self.ball.rect.y + self.ball.velocity_y
        ball_vx = self.ball.velocity_x
        ball_vy = self.ball.velocity_y
        
        print(f"X:{self.ball.rect.x} - Y:{self.ball.rect.x}")
        print(f"X2:{x2} - Y2:{y2}")
        #if self.ball.velocity_x < 0:
        cond = (lambda x2, x: x2 > x) if self.paddle.n == 1 else (lambda x2, x: x2 < x) #!

        while cond(x2, self.paddle.rect.x):
                x2 = x2 + ball_vx
                y2 = y2 + ball_vy
                print(f"Xn:{x2} - Yn:{y2}")
                if y2 <= 0:
                    y2 = 0
                    if ball_vy < 0:
                        ball_vy *= -1
                
                elif y2 >= self.ball.window.get_height():
                    y2 = self.ball.window.get_height()
                    if ball_vy > 0:
                        ball_vy *= -1

                if x2 <= 0:
                    x2 = 0
                    if ball_vx < 0:
                        ball_vx *= -1
                
                elif x2 >= self.ball.window.get_width():
                    x2 = self.ball.window.get_width()
                    if ball_vx > 0:
                        ball_vx *= -1
                pygame.draw.rect(self.ball.window,self.color,pygame.Rect(x2, y2, 10, 10))

        return (x2, y2)
