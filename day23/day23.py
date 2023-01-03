file = open('day23/input.txt', 'r')
lines = file.readlines()


def parse_input(lines):
    grid = []
    for line in lines:
        grid.append(list(line.strip()))
    return grid


def get_elves_position(grid):
    elves = set()
    for i in range(len(grid) - 1, -1, -1):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                elves.add((len(grid) - 1 - i, j))
    return elves


def west_neighbors(elf):
    x, y = elf
    return [
        (x - 1, y + 1),
        (x - 1, y),
        (x - 1, y - 1),
    ]


def east_neighbors(elf):
    x, y = elf
    return [
        (x + 1, y + 1),
        (x + 1, y),
        (x + 1, y - 1),
    ]


def north_neighbors(elf):
    x, y = elf
    return [
        (x - 1, y + 1),
        (x, y + 1),
        (x + 1, y + 1),
    ]


def south_neighbors(elf):
    x, y = elf
    return [
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
    ]


def can_move_north(elf):
    for neighbor in north_neighbors(elf):
        if neighbor in elves:
            return False
    return True


def can_move_south(elf):
    for neighbor in south_neighbors(elf):
        if neighbor in elves:
            return False
    return True


def can_move_east(elf):
    for neighbor in east_neighbors(elf):
        if neighbor in elves:
            return False
    return True


def can_move_west(elf):
    for neighbor in west_neighbors(elf):
        if neighbor in elves:
            return False
    return True


grid = parse_input(lines)
elves = get_elves_position(grid)


print('Can Move north', can_move_north((6, 4)), True)
print('Can Move south', can_move_south((6, 4)), False)
print('Can Move east', can_move_east((6, 4)), True)
print('Can move west', can_move_west((6, 4)), False)
print('Can move west', can_move_west((5, 2)), True)
