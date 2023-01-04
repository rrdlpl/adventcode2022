from collections import defaultdict


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
    blizzards = get_blizzards(grid)
    blizzard_direction = {
        '>': (1, 0),
        'v': (0, 1),
        '<': (-1, 0),
        '^': (0, -1)
    }
    m = len(grid)
    n = len(grid[0])
    for t in range(18):
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

        print()
        print('Minute ', t + 1)
        print()
        show(grid)


def show(grid):
    for g in grid:
        print(''.join(g))


grid = parse_input(lines)

show(grid)

tick(grid)
