import pygame

class Player:
    def __init__(self, Paddle, ball_group):
        self.paddle = Paddle
        self.ball_group = ball_group.sprites()
        self.choiced_ball = self.ball_group[0]
        self.ball = self.ball_group[0]

    def update(self):
        #super().update()
        self.autoMove()
        self.decision()

    def moverY(self,y): #ainda não está em uso
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
        if self.paddle.n == 1:
            bolas_vindo = [b for b in self.ball_group if b.velocity_x < 0]

            for b in bolas_vindo:
                if b.getX() > self.paddle.rect.right:
                    if self.choiced_ball is None or b.getX() < self.choiced_ball.getX():
                        self.setChoicedBall(b)
                        return self.choiced_ball
            return False
        elif self.paddle.n == 2:
            bolas_vindo = [b for b in self.ball_group if b.velocity_x > 0]

            for b in bolas_vindo:
                if b.getX() > self.paddle.rect.right:
                    if self.choiced_ball is None or b.getX() < self.choiced_ball.getX():
                        self.setChoicedBall(b)
                        return self.choiced_ball
            return False
        
    def autoMove(self):
        if self.choiced_ball != None:
            if self.paddle.n == 1:
                self.moverY(self.calcularRota(self.choiced_ball)[1])
            
            elif self.paddle.n == 2:
                if self.decision().velocity_x > 0:
                    if self.paddle.getCenter() < self.calcularRota()[1]:
                        self.paddle.moveDown()
                    elif self.paddle.getCenter() > self.calcularRota()[1]:
                        self.paddle.moveUp()
                    else:
                        self.paddle.stop()

    def calcularRota(self, ball_input):
        x2 = ball_input.rect.x + ball_input.velocity_x
        y2 = ball_input.rect.y + ball_input.velocity_y
        ball_vx = ball_input.velocity_x
        ball_vy = ball_input.velocity_y
        
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
                pygame.draw.circle(ball_input.window,(0,255,0),(x2, y2), ball_input.radius)

        return (x2, y2)

    def setChoicedBall(self, ball):
        if self.choiced_ball == None:
            self.choiced_ball = ball
            if self.choiced_ball != None:
                self.choiced_ball.color = (0,0,255)
        else:
            self.choiced_ball.color = (255,0,0)
            self.choiced_ball = ball
            if self.choiced_ball != None:
                self.choiced_ball.color = (0,0,255)
        return True