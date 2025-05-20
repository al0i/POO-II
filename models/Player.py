class Player:
    def __init__(self, Paddle, Ball):
        self.paddle = Paddle
        self.ball = Ball

    def verifyBallY(self):
        return self.ball.getY()
