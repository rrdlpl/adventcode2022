from collections import defaultdict, deque
from math import lcm


file = open('day24/input.txt', 'r')
lines = file.readlines()


def parse_input(lines):
    grid = []
    for line in lines:
        grid.append(list(line.strip()))
    return grid


def get_blizzards(grid):
    blizzards = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '>' or grid[i][j] == '<' or grid[i][j] == 'v' or grid[i][j] == '^':
                blizzards.append((i, j, grid[i][j]))
    return blizzards


def tick(start, end, t):
    global best_time
    print('Start', start)
    print('End', end)
    minute = t
    queue = deque()
    best_time = 1e9
    path_time = defaultdict(lambda: 1e9)
    path_time[(start, minute)] = 0
    queue.append((start, minute))

    def get_next_moves(current_position):
        x, y = current_position
        return [
            (x, y),
            (x, y - 1),
            (x + 1, y),
            (x, y + 1),
            (x - 1, y)
        ]

    def move(next_position, t, best_ellapsed_time):
        global best_time
        x, y = next_position

        if next_position != start and next_position != end:
            if x <= 0 or y <= 0 or x >= m - 1 or y >= n - 1:
                return
        t %= cycles

        new_time = best_ellapsed_time + 1
        if new_time >= best_time:
            return

        map = maps[t]
        if len(map[(x, y)]) > 0:
            return
        if new_time < path_time[(next_position, t)]:
            path_time[(next_position, t)] = new_time
            queue.append((next_position, t))

        if next_position == end and new_time < best_time:
            best_time = new_time

    while len(queue) > 0:
        current_position, minute = queue.popleft()
        if current_position == end:
            continue

        best_ellapsed_time = path_time[(current_position, minute)]

        if best_ellapsed_time >= best_time:
            continue

        for next_position in get_next_moves(current_position):
            move(next_position, minute + 1, best_ellapsed_time)

    return int(best_time)


def show(grid):
    for g in grid:
        print(''.join(g))


def prebuild_maps(cycles, grid):
    maps = []
    blizzards = get_blizzards(grid)

    blizzard_direction = {
        '>': (1, 0),
        'v': (0, 1),
        '<': (-1, 0),
        '^': (0, -1)
    }

    colliding_blizzards = defaultdict(lambda: set())

    for i, j, direction in blizzards:
        colliding_blizzards[(i, j)].add(direction)

    maps.append(colliding_blizzards)

    for _ in range(cycles):
        colliding_blizzards = defaultdict(lambda: set())
        for i in range(len(blizzards)):
            bi, bj, direction = blizzards[i]
            x, y = blizzard_direction[direction]
            if grid[bi + y][bj + x] == '#':
                bi = (bi + 3 * y) % m
                bj = (bj + 3 * x) % n
            else:
                bi = bi + y
                bj = bj + x

            colliding_blizzards[(bi, bj)].add(direction)
            blizzards[i] = (bi, bj, direction)
        maps.append(colliding_blizzards)
        print('Building map', _, '/', cycles)
    return maps


grid = parse_input(lines)
m = len(grid)
n = len(grid[0])

s = (0, 1)
e = (m - 1, n - 2)

cycles = lcm(m - 2, n - 2)
maps = prebuild_maps(cycles, grid)

first_time = tick(s, e, 0)

print('Solution 1', first_time)

second_time = tick(e, s, first_time)
print('Going back to start', second_time)

third_time = tick(s, e, first_time + second_time)
print('Going back to end', third_time)

print('Solution 2', first_time + second_time + third_time)
