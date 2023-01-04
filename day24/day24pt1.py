from collections import defaultdict, deque
from copy import deepcopy
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


def tick(grid):
    m = len(grid)
    n = len(grid[0])

    start = (0, 1)
    end = (m - 1, n - 2)
    maps = prebuild_maps(lcm(m - 2, n - 2), grid)

    def get_next_moves(E):
        i, j = E
        return [
            (i, j + 1),
            (i + 1, j),
            (i, j - 1),
            (i - 1, j)
        ]
    t = 0
    queue = deque()
    queue.append((start, t))

    while len(queue) > 0:

        # colliding_blizzards = defaultdict(lambda: set())
        E, t = queue.popleft()
        map = maps[(t + 1) % len(maps)]
        # show(map)

        for move in get_next_moves(E):
            if move == end:
                print('Solution 1 -> Minute', t + 1)
                map[end[0]][end[1]] = 'E'
                show(map)
                return

        if map[E[0]][E[1]] == '.':
            queue.append((E, t + 1))

        for move in get_next_moves(E):
            next_row, next_col = move
            if next_row >= 0 and next_col >= 0 and next_row < m and next_col < n and map[next_row][next_col] == '.':
                # if len(colliding_blizzards[E]) == 0:
                #     map[E[0]][E[1]] = '.'
                # map[next_row][next_col] = 'E'
                E = move
                queue.append((move, t + 1))

        # print()
        t += 1
        # print('Minute ', t)
        # print()
        # show(map)


def show(grid):
    for g in grid:
        print(''.join(g))


def prebuild_maps(cycles, grid):

    maps = [deepcopy(grid)]
    blizzards = get_blizzards(grid)

    blizzard_direction = {
        '>': (1, 0),
        'v': (0, 1),
        '<': (-1, 0),
        '^': (0, -1)
    }
    m = len(grid)
    n = len(grid[0])

    for _ in range(cycles):
        colliding_blizzards = defaultdict(lambda: set())
        for i in range(len(blizzards)):
            bi, bj, direction = blizzards[i]
            x, y = blizzard_direction[direction]
            grid[bi][bj] = '.'
            if grid[bi + y][bj + x] == '#':
                bi = (bi + 3 * y) % m
                bj = (bj + 3 * x) % n
            else:
                bi = bi + y
                bj = bj + x

            colliding_blizzards[(bi, bj)].add(direction)
            blizzards[i] = (bi, bj, direction)

            for key in colliding_blizzards:
                if len(colliding_blizzards[key]) == 0:
                    continue
                i, j = key
                if len(colliding_blizzards[key]) == 1:
                    grid[i][j] = list(colliding_blizzards[key])[0]
                else:
                    grid[i][j] = str(len(colliding_blizzards[key]))
        maps.append(deepcopy(grid))

    # for t in range(cycles):
    #     print('Minute ', t)
    #     print()
    #     show(maps[t])
    #     print()
    return maps


grid = parse_input(lines)

tick(grid)
