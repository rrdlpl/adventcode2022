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
        self.instruction = 0

    def add_air(self, h):
        for _ in range(h + 1):
            self.stack.append(list('|' + '.' * self.width + '|'))

    def print(self):
        if not DEBUG:
            return
        for i in range(len(self.stack) - 1,  -1, -1):
            t = ''.join(self.stack[i])
            print(t)

    def add_shape(self, shape, jet_instructions):
        aux = self.get_heighst_rock()
        # y = len(self.stack) - 1 if aux == -1 else aux
        # print('aux', aux)
        if aux == -1:
            shape.start(2, len(self.stack) - 1)
        else:
            shape.start(2, aux + 4)

        length = len(jet_instructions)

        # print('New rock falling')
        while not shape.is_at_rest(self.resting_rocks):
            self.draw(shape, '#')
            self.print()
            self.draw(shape, '.')
            if jet_instructions[self.instruction % length] == '<':

                shape.move_left(0, self.resting_rocks)
            else:

                shape.move_right(self.width, self.resting_rocks)

            shape.fall(self.resting_rocks)
            self.draw(shape, '#')
            self.print()
            self.draw(shape, '.')
            self.instruction += 1

        self.adjust_cave_height()
        self.draw(shape, '#')

    def adjust_cave_height(self):

        y = self.get_heighst_rock()

        if len(self.stack) - 1 - y <= 3:
            height_needed = abs(len(self.stack) - (y + 3))

            self.add_air(height_needed)

    def get_heighst_rock(self):
        y = -1
        for rock in self.resting_rocks:
            y = max(y, rock[1])
        return y

    def throw_shapes(self, shapes, jet_instructions, n):
        for i in range(n):
            shape = shapes[i % len(shapes)]
            self.add_shape(shape, jet_instructions)

    def draw(self, shape, char):
        if not DEBUG:
            return
        for point in shape.points:
            i, j = point
            if j < len(self.stack):
                self.stack[j][i + 1] = char


class Shape:
    def __init__(self, points, name) -> None:
        self.points = points
        self.original_points = points.copy()
        self.name = name

    def start(self, start_x, start_y):
        self.points = self.original_points.copy()

        for i in range(len(self.points)):
            x, y = self.points[i]
            self.points[i] = (x + start_x, start_y + y)

    def fall(self, resting_rocks: set):
        def can_keep_falling(point, resting_rocks):
            x, y = point
            if y - 1 == 0 or (x, y - 1) in resting_rocks:
                for point in self.points:
                    resting_rocks.add(point)
                return False
            return True

        print('Rock falls one unit:')
        for point in self.points:
            if not can_keep_falling(point, resting_rocks):
                return

        for i in range(len(self.points)):
            x, y = self.points[i]
            self.points[i] = (x, y - 1)

    def is_at_rest(self, resting_rocks: set):
        aux = sorted(self.points, key=itemgetter(1))
        x, y = aux[0]
        # print('lowest', x, y)
        # print(self.points)
        if y == 0 or (x, y) in resting_rocks:
            return True
        return False

    def move_right(self, right_wall, resting_rocks):

        for point in self.points:
            x, y = point
            if x + 1 >= right_wall or (x + 1, y) in resting_rocks:
                # print('Jet of gas pushes rock right, but nothing happens: ')
                return
        # print('Jet of gas pushes rock right:')
        for i in range(len(self.points) - 1, -1, -1):
            x, y = self.points[i]
            self.points[i] = (x + 1, y)

    def move_left(self, left_wall, resting_rocks):
        for point in self.points:
            x, y = point
            if x - 1 < left_wall or (x - 1, y) in resting_rocks:
                # print('Jet of gas pushes rock left, but nothing happens: ')
                return

        # print('Jet of gas pushes rock left:')
        for i in range(len(self.points)):
            x, y = self.points[i]
            if x - 1 < left_wall or (x - 1, y) in resting_rocks:
                break
            self.points[i] = (x - 1, y)


file = open('day17/input.txt', 'r')
lines = file.readlines()


start_time = time.time()

DEBUG = False

tetris = Tetris()
tetris.add_air(3)
horizontal_line = Shape([(0, 0), (1, 0), (2, 0), (3, 0)], 'horizontal')
vertical_line = Shape([(0, 0), (0, 1), (0, 2), (0, 3)], 'vertical')

square = Shape([(0, 0), (0, 1), (1, 0), (1, 1)], 'square')
L = Shape([(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)], 'L')
cross = Shape([(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)], 'cross')


shapes = [horizontal_line, cross, L, vertical_line, square]

tetris.throw_shapes(shapes, lines[0].strip(), 2022)
print('Solution 1', tetris.get_heighst_rock())


end_time = time.time()

print('Time ellapsed', (end_time - start_time) * 1000)

file.close()

100_000_000_0000
