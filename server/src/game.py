import random


class point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class vector():
    def __init__(self, x=0, y=0):
        if (type(x) is vector or type(x) is point):
            if (y == 0):
                self.x = x.x
                self.y = x.y
            else:
                self.x = y.x - x.x
                self.y = y.y - x.y
        else:
            self.x = x
            self.y = y

    def __add__(self, other):
        if (type(other) == point):  
            return point(self.x + other.x, self.y + other.y)
        return vector(self.x + other.x, self.y + other.y)

    def __radd__(self, other):
        if (type(other) == point):  
            return point(self.x + other.x, self.y + other.y)
        return vector(self.x + other.x, self.y + other.y)
    
    def __iadd__(self, other):  
        self.x += other.x
        self.y += other.y

    def __sub__(self, other):
        return vector(self.x - other.x, self.y - other.y)

    def __rsub__(self, other):
        if (type(other) is point):
            return point(self.x - other.x, self.y - other.y)
        return vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return vector(self.x / other, self.y / other)
    
    def __rmul__(self, other):
        return vector(self.x / other, self.y / other)
        
    def __imul__(self, other):  
        self.x *= other
        self.y *= other


class player():
    def __init__(self):
        self.pos = point()
        self.max_hp = 0
        self.speed = vector()
        self.speed_abs = 0
        self.max_speed = 5
        self.acc = 0

    def move(self, dt):
        self.pos += self.speed * self.speed_abs * dt + (self.acc * dt * dt) / 2
        
    def set_controls(self, 
