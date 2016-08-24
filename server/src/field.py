import random 

Empty = 0
Wall = 1
Stone = 2

class cell():
    def __init__(self, x, y, t=Empty):
        self.type = t
        self.x = x
        self.y = y


def gen_field(x, y):
    arr = [[cell(i, j) for j in range(y)] for i in range(x)]
    for i in range(x):  
        arr[i][0] = cell(i, 0, Stone)
        arr[i][-1] = cell(i, y - 1, Stone)
    for j in range(y):
        arr[0][j] = cell(0, j, Stone)
        arr[-1][j] = cell(x - 1, j, Stone)
    for i in range(2 * (x + y)):
        wall_x, wall_y = random.randint(1, x - 1), random.randint(1, y - 1)
        arr[wall_x][wall_y] = cell(wall_x, wall_y, Wall)
    return arr
