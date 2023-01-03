from collections import defaultdict


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
                elves.add((j, len(grid) - 1 - i))
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


def part_one(elves):
    moves = ['north', 'south', 'west', 'east']

    for _ in range(10):
        new_elves = set()
        proposed_moves = defaultdict(lambda: [])

        for elf in elves:
            if can_move_north(elf) and can_move_south(elf) and can_move_east(elf) and can_move_west(elf):
                new_elves.add(elf)
                continue

            x, y = elf
            for move in moves:
                if move == 'north' and can_move_north(elf):
                    proposed_moves[(x, y + 1)].append(elf)
                    break

                if move == 'south' and can_move_south(elf):
                    proposed_moves[(x, y - 1)].append(elf)
                    break

                if move == 'west' and can_move_west(elf):
                    proposed_moves[(x - 1, y)].append(elf)
                    break

                if move == 'east' and can_move_east(elf):
                    proposed_moves[(x + 1, y)].append(elf)
                    break

        for key in proposed_moves:
            if len(proposed_moves[key]) == 1:
                new_elves.add(key)
            else:
                for static_elf in proposed_moves[key]:
                    new_elves.add(static_elf)
        elves = new_elves
        moves.append(moves.pop(0))

    min_x = min(x for x, _ in elves)
    min_y = min(y for _, y in elves)
    max_x = max(x for x, _ in elves)
    max_y = max(x for x, _ in elves)

    print('Solution 1', (max_x - min_x + 1) * (max_y - min_y + 1) - len(elves))


# print('Can Move north', can_move_north((6, 4)), True)
# print('Can Move south', can_move_south((6, 4)), False)
# print('Can Move east', can_move_east((6, 4)), True)
# print('Can move west', can_move_west((6, 4)), False)
# print('Can move west', can_move_west((5, 2)), True)
grid = parse_input(lines)
elves = get_elves_position(grid)
# print('Elves', elves)
part_one(elves)
