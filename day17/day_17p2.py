from collections import Counter, defaultdict, deque

from math import lcm
import time
import os
from operator import itemgetter


# from numpy import range


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class Tetris:
    def __init__(self, width=7) -> None:
        self.stack = [
            list('+' + '_' * width + '+')
        ]
        self.width = width
        self.resting_rocks = set()
        self.instruction = 0
        self.heighest = 0
        self.y_dict = defaultdict(lambda: 0)
        self.floor = 0

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
        aux = self.heighest

        shape.start(2, aux + 4)
        # if aux == -1:
        #     shape.start(2, len(self.stack) - 1)
        # else:
        #     shape.start(2, aux + 4)

        length = len(jet_instructions)

        while not shape.is_at_rest(self.resting_rocks, self.floor):
            if jet_instructions[self.instruction % length] == '<':
                shape.move_left(0, self.resting_rocks)
            else:
                shape.move_right(self.width, self.resting_rocks)

            shape.fall(self.resting_rocks, self.floor)
            self.instruction += 1

        for i in range(len(shape.points)):
            _, y = shape.points[i]

            self.heighest = max(self.heighest, y)
            self.y_dict[y] += 1
            if self.width == self.y_dict[y]:
                self.y_dict.clear()
                self.floor = y
                result = list(filter(lambda x: x[1] >= y, self.resting_rocks))
                self.resting_rocks = set(result)

        self.draw(shape, '#')

    def throw_shapes(self, shapes, jet_instructions, n):
        seen = set()
        for i in range(n):
            shape = shapes[i % len(shapes)]
            self.add_shape(shape, jet_instructions)
            landing = shape.get_landing_position()

            # if (i % 5, jet_instructions[i % n], landing) in seen:
            #     print('Cycle found at', i)
            land_x, land_y = landing

            # if (i % 5, jet_instructions[i % len(jet_instructions)], land_x, land_y - self.heighest) in seen:
            #     print('Cycle found at ', i)
            #     return
            # seen.add(
            #     (i % 5, jet_instructions[i % len(jet_instructions)], land_x, land_y - self.heighest))

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

    def fall(self, resting_rocks: set, floor):
        def can_keep_falling(point, resting_rocks):
            x, y = point
            if y - 1 == floor or (x, y - 1) in resting_rocks:
                for i in range(len(self.points)):
                    resting_rocks.add(self.points[i])
                return False
            return True

        # print('Rock falls one unit:')
        for i in range(len(self.points)):
            if not can_keep_falling(self.points[i], resting_rocks):
                return

        for i in range(len(self.points)):
            x, y = self.points[i]
            self.points[i] = (x, y - 1)

    def get_landing_position(self):
        min_x = min([x for x, _ in self.points])
        max_y = max([y for _, y in self.points])
        return (min_x, max_y)

    def is_at_rest(self, resting_rocks: set, floor):
        aux = sorted(self.points, key=itemgetter(1))
        x, y = aux[0]
        if y == floor or (x, y) in resting_rocks:
            return True
        return False

    def move_right(self, right_wall, resting_rocks):
        for i in range(len(self.points)):
            x, y = self.points[i]
            if x + 1 >= right_wall or (x + 1, y) in resting_rocks:
                return
        for i in range(len(self.points) - 1, -1, -1):
            x, y = self.points[i]
            self.points[i] = (x + 1, y)

    def move_left(self, left_wall, resting_rocks):
        for i in range(len(self.points)):
            x, y = self.points[i]
            if x - 1 < left_wall or (x - 1, y) in resting_rocks:
                return

        for i in range(len(self.points)):
            x, y = self.points[i]
            if x - 1 < left_wall or (x - 1, y) in resting_rocks:
                break
            self.points[i] = (x - 1, y)


file = open('day17/input.txt', 'r')
lines = file.readlines()


start_time = time.time()

DEBUG = False


horizontal_line = Shape([(0, 0), (1, 0), (2, 0), (3, 0)], 'horizontal')
vertical_line = Shape([(0, 0), (0, 1), (0, 2), (0, 3)], 'vertical')

square = Shape([(0, 0), (0, 1), (1, 0), (1, 1)], 'square')
L = Shape([(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)], 'L')
cross = Shape([(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)], 'cross')


shapes = [horizontal_line, cross, L, vertical_line, square]


def part_two():
    def get_board(board):
        strings = []
        miny = max(y for x, y in list(board))
        for y in range(1, miny):
            strings.append(''.join(
                ['#' if (i, y) in board else ' ' for i in range(7)]))
        return strings[::-1]

    # instructions = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
    instructions = lines[0]
    mcd = lcm(5, len(instructions))
    n = 100_000_000_0000 // mcd
    missing = 100_000_000_0000 - (n * mcd)

    print('Mcd', mcd)
    print('n', n)
    print('missing', missing)

    i = 2

    tetris = Tetris(7)
    tetris.add_air(3)

    tetris.throw_shapes(shapes, instructions, 330)
    print('Part one', tetris.heighest)
    estimated = tetris.heighest

    test = [0]
    while True:
        tetris = Tetris(7)
        tetris.add_air(3)
        # tetris.instruction = 0
        tetris.throw_shapes(shapes, instructions, i)
        # print('I am on instruction', tetris.instruction % len(instructions))
        # print(i,  i * mcd, 'Heighest at ', tetris.heighest,
        #       'Expected =', estimated * i, 'Missing', (tetris.heighest))
        test.append(abs(tetris.heighest))

        if len(test) == 100 + 1:
            break

        i += 1

    sum = 0
    cycle = []
    for i in range(1, len(test)):
        # print('Finding cycle', test[i] - test[i - 1])
        sum += test[i] - test[i - 1]
        cycle.append(str(test[i] - test[i - 1]))
        if i % 5 == 0:
            print('sum += ' + ' + '.join(cycle),
                  ' # rock', i, 'heighest', test[i])
            cycle = []


part_two()
end_time = time.time()

print('Time ellapsed', (end_time - start_time), 'secs')


file.close()

100_000_000_0000
1000_000_000_000
