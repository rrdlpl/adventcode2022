
import math
import time


file = open('day14/input.txt', 'r')
lines = file.readlines()

directions = [(0, 1), (-1, 1), (1, 1)]


class Vector2D:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return repr((self.x, self.y))

    def to_tuple(self):
        return (self.x, self.y)


def parse_input(lines):
    rock_vectors = []

    for line in lines:
        line = line.strip()
        line = line.split('->')
        rocks = []
        for coord in line:
            coord = coord.strip()
            coord = coord.split(',')
            x = int(coord[0])
            y = int(coord[1])
            rocks.append(Vector2D(x, y))

        rock_vectors.append(rocks)

    rocks_positions = set()
    abyss_y = -1
    for rocks in rock_vectors:
        current = rocks[0]
        rocks_positions.add(current.to_tuple())
        abyss_y = max(abyss_y, current.y)
        for i in range(1, len(rocks)):
            destination = rocks[i]
            direction = destination - current
            for _ in range(math.floor(abs(direction.x))):
                dx = math.floor(abs(direction.x) / direction.x)
                current = Vector2D(current.x + dx, current.y)
                rocks_positions.add(current.to_tuple())

                abyss_y = max(abyss_y, current.y)

            for _ in range(math.floor(abs(direction.y))):
                dy = math.floor(abs(direction.y) / direction.y)
                current = Vector2D(current.x, current.y + dy)
                rocks_positions.add(current.to_tuple())
                abyss_y = max(abyss_y, current.y)

    # print('Is 500, 9 in rocks ?', (500, 9) in rocks_positions)
    # print('Is 499, 9 in rocks ?', (499, 9) in rocks_positions)
    # print('Is 501, 9 in rocks ?', (501, 9) in rocks_positions)
    print('abyss starts at', abyss_y)
    # print('rocks ', rocks_positions)
    return rocks_positions, abyss_y


def is_at_rest(start, rocks_positions):
    x, y = start
    blocked = True

    for direction in directions:
        dx, dy = direction
        next_move = (x + dx, y + dy)
        blocked = blocked & (next_move in rocks_positions)
        if not blocked:
            return blocked, next_move

    return blocked, None


def pour_sand(position, rocks_positions, abyss_y, sand):
    if position[1] >= abyss_y:
        return
    is_resting, next_move = is_at_rest(position, rocks_positions)
    if is_resting:
        sand.add(position)
        rocks_positions.add(position)
        return
    pour_sand(next_move, rocks_positions, abyss_y, sand)


def part_one():
    start = (500, 0)
    rocks_positions, abyss_y = parse_input(lines)
    sand = set()

    while True:
        size = len(sand)
        pour_sand(start, rocks_positions, abyss_y, sand)
        if size == len(sand):
            break
    print('Solution 1', len(sand))


start_time = time.time()

part_one()
# print('is at rest 500, 7', is_at_rest((500, 7), rocks_positions))
# print('is at rest 500, 8', is_at_rest((500, 8), rocks_positions))


end_time = time.time()


print('Time ellapsed', (end_time - start_time) * 1000)

file.close()
