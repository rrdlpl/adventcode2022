from collections import defaultdict, deque
from copy import deepcopy


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
    bliz = get_blizzards(grid)
    blizzard_direction = {
        '>': (1, 0),
        'v': (0, 1),
        '<': (-1, 0),
        '^': (0, -1)
    }
    m = len(grid)
    n = len(grid[0])
    print('Rows', m)
    print('Cols', n)
    start = (0, 1)
    end = (m - 1, n - 2)

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
    queue.append((start, deepcopy(grid), deepcopy(bliz), t))

    while len(queue) > 0:

        colliding_blizzards = defaultdict(lambda: set())
        E, map, blizzards, t = queue.popleft()

        for i in range(len(blizzards)):
            bi, bj, direction = blizzards[i]
            x, y = blizzard_direction[direction]
            map[bi][bj] = '.'
            if map[bi + y][bj + x] == '#':
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
                map[i][j] = list(colliding_blizzards[key])[0]
            else:
                map[i][j] = str(len(colliding_blizzards[key]))

        for move in get_next_moves(E):
            if move == end:
                print('Solution 1 -> Minute', t + 1)
                map[E[0]][E[1]] = 'E'
                show(map)
                return
        if len(colliding_blizzards[E]) == 0:
            queue.append((E, deepcopy(map), deepcopy(blizzards), t + 1))

        for move in get_next_moves(E):
            next_row, next_col = move
            if next_row >= 0 and next_col >= 0 and next_row < m and next_col < n and map[next_row][next_col] == '.':
                if len(colliding_blizzards[E]) == 0:
                    map[E[0]][E[1]] = '.'
                map[next_row][next_col] = 'E'
                E = move
                queue.append((move, deepcopy(map), deepcopy(blizzards), t + 1))

        print()
        t += 1
        print('Minute ', t)
        print()
        # show(map)


def show(grid):
    for g in grid:
        print(''.join(g))


grid = parse_input(lines)

print('Initial State:')
show(grid)
print()

tick(grid)
