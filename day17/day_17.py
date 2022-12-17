from collections import defaultdict, deque
import time
import os
from operator import itemgetter


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class Tetris:
    def __init__(self, width=7) -> None:
        self.stack = [
            list('+' + '_' * width + '+')
        ]
        self.width = width
        self.height = 0
        self.resting_rocks = set()

    def add_air(self):
        for _ in range(4):
            self.stack.append(list('|' + '.' * self.width + '|'))

    def print(self):
        for i in range(len(self.stack) - 1,  -1, -1):
            print(''.join(self.stack[i]))

    def add_shape(self, shape):
        y = len(self.stack) - 1
        shape.start(2, y)

        while not shape.is_at_rest(self.resting_rocks):
            self.draw(shape, '#')
            self.print()
            self.draw(shape, '.')
            shape.fall(self.resting_rocks)
            # shape.move_left(0)
            time.sleep(1)
            # clear()

        self.draw(shape, '#')
        for point in shape.points:
            self.resting_rocks.add(point)
        print('Resting', self.resting_rocks)
        print('stack at bottom', ''.join(self.stack[1]))

    def throw_shapes(self, shapes):
        for shape in shapes:
            self.add_shape(shape)

    def draw(self, shape, char):
        for point in shape.points:
            i, j = point
            if j < len(self.stack):
                self.stack[j][i + 1] = char


class Shape:
    def __init__(self, points) -> None:
        self.points = points
        # self.height = height

    def start(self, start_x, start_y):
        for i in range(len(self.points)):
            x, y = self.points[i]
            self.points[i] = (x + start_x, start_y + y)

    def fall(self, resting_rocks: set):
        aux = sorted(self.points, key=itemgetter(1))
        x, y = aux[0]
        if y - 1 == 0 or (x, y - 1) in resting_rocks:
            print('Resting rocks', resting_rocks)
            for point in aux:
                resting_rocks.add(point)
            return
        for i in range(len(self.points)):
            x, y = self.points[i]
            if y - 1 == 0 or (x, y - 1) in resting_rocks:
                break
            self.points[i] = (x, y - 1)

    def is_at_rest(self, resting_rocks: set):
        aux = sorted(self.points, key=itemgetter(1))
        x, y = aux[0]
        print('lowest', x, y)
        print(self.points)
        if y == 0 or (x, y) in resting_rocks:
            return True
        return False

    def move_right(self, right_wall):
        for i in range(len(self.points) - 1, -1, -1):
            x, y = self.points[i]
            if x + 1 >= right_wall:
                break
            self.points[i] = (x + 1, y)

    def move_left(self, left_wall):
        for i in range(len(self.points)):
            x, y = self.points[i]
            if x - 1 < left_wall:
                break
            self.points[i] = (x - 1, y)


file = open('day17/input.txt', 'r')
lines = file.readlines()


start_time = time.time()


tetris = Tetris()
tetris.add_air()
horizontal_line = Shape([(0, 0), (1, 0), (2, 0), (3, 0)])
vertical_line = Shape([(0, 0), (0, 1), (0, 2), (0, 3)])

square = Shape([(0, 0), (0, 1), (1, 0), (1, 1)])
L = Shape([(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)])
cross = Shape([(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)])


shapes = [horizontal_line, cross]

tetris.throw_shapes([horizontal_line, cross])
# tetris.print()

end_time = time.time()

print('Time ellapsed', (end_time - start_time) * 1000)

file.close()
