class Player:
    def __init__(self, Paddle, Ball):
        self.paddle = Paddle
        self.ball = Ball

    def verifyBallY(self):
        return self.ball.getY()

    def moveUp(self):
        self.paddle.moveUp()

    def autoMove(self):
        if self.paddle.getCenter() < self.verifyBallY():
            self.paddle.moveDown()
        elif self.paddle.getCenter() > self.verifyBallY():
            self.paddle.moveUp()
        else:
            pass