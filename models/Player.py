import pygame

class Player:
    def __init__(self, Paddle, ball_group):
        self.paddle = Paddle
        self.ball = ball_group.sprites()[0]
        self.color = (0,255,0)
        self.ball_group = ball_group.sprites()
        self.choiced_ball = self.decision()

    def decision(self):
        
        for b in self.ball_group:
            if b.getX() < choiced_ball.getX() and b.velocity_x < 0:
                choiced_ball.color = (255,0,0)
                choiced_ball = b
        choiced_ball.color = (0,0,255)
        return choiced_ball

    def moveUp(self):
        self.paddle.moveUp()

    def autoMove(self):
        if self.paddle.n == 1:
            if self.paddle.getCenter() < self.calcularRota()[1]:
                self.paddle.moveDown()
            elif self.paddle.getCenter() > self.calcularRota()[1]:
                self.paddle.moveUp()
            else:
                self.paddle.stop()
        
        elif self.paddle.n == 2:
            if self.decision().velocity_x > 0:
                if self.paddle.getCenter() < self.calcularRota()[1]:
                    self.paddle.moveDown()
                elif self.paddle.getCenter() > self.calcularRota()[1]:
                    self.paddle.moveUp()
                else:
                    self.paddle.stop()

    def calcularRota(self):
        x2 = self.choiced_ball.rect.x + self.choiced_ball.velocity_x
        y2 = self.choiced_ball.rect.y + self.choiced_ball.velocity_y
        ball_vx = self.choiced_ball.velocity_x
        ball_vy = self.choiced_ball.velocity_y
        
        cond = (lambda x2, x: x2 > x) if self.paddle.n == 1 else (lambda x2, x: x2 < x) #!

        while cond(x2, self.paddle.rect.x):
                x2 = x2 + ball_vx
                y2 = y2 + ball_vy
                if y2 <= 0:
                    y2 = 0
                    if ball_vy < 0:
                        ball_vy *= -1
                
                elif y2 >= self.choiced_ball.window.get_height():
                    y2 = self.choiced_ball.window.get_height()
                    if ball_vy > 0:
                        ball_vy *= -1

                if x2 <= 0:
                    x2 = 0
                    if ball_vx < 0:
                        ball_vx *= -1
                
                elif x2 >= self.choiced_ball.window.get_width():
                    x2 = self.choiced_ball.window.get_width()
                    if ball_vx > 0:
                        ball_vx *= -1
                pygame.draw.rect(self.choiced_ball.window,self.color,pygame.Rect(x2, y2, 10, 10))

        return (x2, y2)
