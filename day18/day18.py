

from collections import deque


cubes = [
]

file = open('day18/input.txt', 'r')
lines = file.readlines()

for line in lines:
    line = [int(l) for l in line.strip().split(',')]
    cube = (line[0], line[1], line[2])
    cubes.append(cube)


total = len(cubes) * 6
print('total area', total)


print('Solution 1', total)


def part_two(input):
    cubes = set(input)

    def get_neighbors(cube):
        x, y, z = cube
        return [
            (x - 1, y, z),
            (x + 1, y, z),
            (x, y - 1, z),
            (x, y + 1, z),
            (x, y, z - 1),
            (x, y, z + 1),
        ]

    def is_air(cube, air_cubes,  mins, maxes):
        x, y, z = cube
        min_x, min_y, min_z = mins
        max_x, max_y, max_z = maxes
        return x >= min_x - 1 and x <= max_x + 1 \
            and y >= min_y - 1 and y <= max_y + 1 \
            and min_z - 1 <= z and z <= max_z + 1 \
            and cube not in cubes \
            and cube not in air_cubes

    min_x = min([x for x, _, _ in cubes])
    min_y = min([y for _, y, _ in cubes])
    min_z = min([z for _, _, z in cubes])

    max_x = max([x for x, _, _ in cubes])
    max_y = max([y for _, y, _ in cubes])
    max_z = max([z for _, _, z in cubes])

    air_cubes = {(min_x - 1, min_y - 1, min_z - 1)}
    queue = deque()

    queue.append((min_x - 1, min_y - 1, min_z - 1))

    while queue:
        top = queue.popleft()
        for cube in get_neighbors(top):
            if is_air(cube, air_cubes, (min_x, min_y, min_z), (max_x, max_y, max_z)):
                air_cubes.add(cube)
                queue.append(cube)

    print('print air cubes', air_cubes)
    print('air cube length', len(air_cubes))

    sum = 0
    for cube in cubes:
        neighbors = get_neighbors(cube)
        for neighbor in neighbors:
            if neighbor in air_cubes:
                sum += 1
    print('Sum', sum)


part_two(cubes)
