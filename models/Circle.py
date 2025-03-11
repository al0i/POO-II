from models.Ball import *

class Circle(Ball):
    def __init__(self, window):
        super().__init__(window)
        self.radius = 400
        self.larger = 2
        self.x = 1280/2
        self.y = 720/2
        self.velocity_x = random.choice([-5,5])
        self.velocity_y = random.choice([-5,5])
        self.color = (255,255,255) #branco

    def draw(self):
        pygame.draw.circle(self.window,self.color,(self.x, self.y),self.radius,self.larger)