from paddle import Paddle

class Paddle2(Paddle):
    def __init__(self):
        super().__init__()
        self.goto(x=-350, y=0)
