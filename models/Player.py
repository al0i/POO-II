import pygame

class Player:
    def __init__(self, Paddle, ball_group):
        self.paddle = Paddle
        #self.ball = ball_group.sprites()[0]
        self.color = (0,255,0)
        self.ball_group = ball_group.sprites()
        self.choiced_ball = self.ball_group[0]
        self.ball = self.ball_group[0]

    def moverY(self,y):
        if y < self.paddle.getCenter():
            self.paddle.moveUp()
        elif y > self.paddle.getCenter():
            self.paddle.moveDown()
        else:
            return False
        return True


    def abracar(self):
        y = 0
        for b in self.ball_group:
            self.calcularRota(b)
            y = self.calcularRota(b)[1]
        self.moverY(y)

    def showBallsRoute(self):
        for b in self.ball_group:
            self.calcularRota(b)
            

    
    def decision(self):
        bolas_vindo = []
        #bolas_voltando = []

        for b in self.ball_group:
            if b.velocity_x < 0:
                bolas_vindo.append(b)
            else:
                if b in bolas_vindo:
                    bolas_vindo.remove(b)
                else:
                    pass

        #Das bolas que estão vindo, escolhe qual seguir
        for b in bolas_vindo:
            if b.velocity_x < 0 and b.rect.x > self.paddle.rect.x:
                if b.getX() < self.choiced_ball.getX():
                    self.choiced_ball.color = (255,0,0)
                    self.choiced_ball = b
        self.choiced_ball.color = (0,0,255)
        return self.choiced_ball

    def autoMove(self):
        if self.paddle.n == 1:
            if self.paddle.getCenter() < self.calcularRota(self.choiced_ball)[1]:
                self.paddle.moveDown()
            elif self.paddle.getCenter() > self.calcularRota(self.choiced_ball)[1]:
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
                pygame.draw.rect(ball_input.window,self.color,pygame.Rect(x2, y2, 10, 10))

        return (x2, y2)
