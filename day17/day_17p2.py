from collections import defaultdict, deque

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
        self.heighest = -1
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
        if aux == -1:
            shape.start(2, len(self.stack) - 1)
        else:
            shape.start(2, aux + 4)

        length = len(jet_instructions)

        while not shape.is_at_rest(self.resting_rocks, self.floor):
            # self.draw(shape, '#')
            # self.print()
            # self.draw(shape, '.')
            if jet_instructions[self.instruction % length] == '<':
                shape.move_left(0, self.resting_rocks)
            else:
                shape.move_right(self.width, self.resting_rocks)

            shape.fall(self.resting_rocks, self.floor)
            # self.draw(shape, '#')
            # self.print()
            # self.draw(shape, '.')
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
        for i in range(n):
            if i > 0 and i % 1_000_000 == 0:
                print(i // 1_000_000, '/', n // 1_000_000)

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


# def part_two():
#     def formula(shapes, instruction, iterations, x):
#         print('There are ', len(shapes), ' shapes')
#         print('There are', len(instruction), ' instructions')
#         mcd = lcm(len(shapes), len(instruction), x)
#         print('(mcd)', mcd)
#         n = iterations // mcd
#         print('n =', n)
#         missing = iterations - n * mcd
#         print('There are ', missing, ' missing')
#         cycleTetris = Tetris(7)
#         cycleTetris.add_air(3)

#         cycleTetris.throw_shapes(shapes, instruction, mcd)

#         missingTetris = Tetris(7)
#         missingTetris.add_air(3)
#         missingTetris.throw_shapes(shapes, instruction, missing)

#         print('Cycle heighst', cycleTetris.heighest)
#         print('Missing parts heights', missingTetris.heighest)

#         # + (missing // len(instruction))
#         # - (iterations // len(instruction))
#         return (cycleTetris.heighest * n) + (missingTetris.heighest) - (iterations // len(instruction))

#     def test_input():
#         test = Tetris(7)
#         test.add_air(3)
#         test.throw_shapes(
#             shapes, '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>', 2022)
#         print('Solution 1', test.heighest, 'Expected', 3068)
#         real = Tetris(7)
#         real.add_air(3)
# #        real.throw_shapes(shapes, lines[0], N)
#         print('Real input solution 1', real.heighest, 3119)
#         return real.heighest

#     N = 100_000_000_0000
#     R = test_input()
# F = formula(shapes, lines[0], N)

# print('Test', formula(
#     shapes, '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>', N) - 1514285714288)

# print('Error ', R, ' - ', F, ' = ', R - F)


def part_two():
    def get_board(board):
        strings = []
        miny = max(y for x, y in list(board))
        for y in range(1, miny):
            strings.append(''.join(
                ['#' if (i, y) in board else ' ' for i in range(7)]))
        #     print()
        # print("-"*15)
        return strings[::-1]

    def find_cycle(board):
        key = {}
        for i,  b in enumerate(board):
            if b in key:
                print('Found cycle at', i, b)
            else:
                key[b] = b

    instructions = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
    # instructions = lines[0]
    mcd = lcm(5, len(instructions))
    n = 100_000_000_0000 // mcd
    missing = 100_000_000_0000 - (n * mcd)

    print('Mcd', mcd)
    print('n', n)
    print('missing', missing)

    tetris = Tetris(7)
    missing_tetris = Tetris(7)
    tetris.add_air(3)
    missing_tetris.add_air(3)

    tetris.throw_shapes(shapes, instructions, mcd)

    board = get_board(tetris.resting_rocks)
    for b in board:
        print(b)

    # find_cycle(board)

    print('Highest before', tetris.heighest)

    missing_tetris.throw_shapes(shapes, instructions, missing)

    highest = n * (tetris.heighest - 7) + missing_tetris.heighest
    print('Highest', highest)


part_two()
end_time = time.time()

print('Time ellapsed', (end_time - start_time), 'secs')


file.close()

100_000_000_0000
1000_000_000_000
