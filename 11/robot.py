
class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = (0, 1)

    def step(self, direction):
        if direction == 0:
            self.direction = (-self.direction[1], self.direction[0])
        elif direction == 1:
            self.direction = (self.direction[1], -self.direction[0])
        else:
            assert False, 'Invalid direction'

        self.x += self.direction[0]
        self.y += self.direction[1]


    @property
    def position(self):
        return self.x, self.y
