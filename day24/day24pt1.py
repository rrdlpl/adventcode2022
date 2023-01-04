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
            a = grid[i][j]
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
    for t in range(2):

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

            grid[bi][bj] = direction
            blizzards[i] = (bi, bj, direction)

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
