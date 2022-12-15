
from collections import deque
import math
import re
import time


file = open('day15/input.txt', 'r')
lines = file.readlines()


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

    def get_radius(self):
        return abs(self.x) + abs(self.y)

    def __abs__(self):
        """Absolute value (magnitude) of the vector."""
        return math.sqrt(self.x**2 + self.y**2)

    def distance_to(self, other):
        return abs(self - other)

    def __hash__(self) -> int:
        return (self.x, self.y).__hash__()


def parse_input(lines):
    sensors = {}

    for line in lines:
        line = line.strip()
        array = [int(s) for s in re.findall(r'-?\d+', line)]
        sx, sy, bx, by = array
        sensors[Vector2D(sx, sy)] = Vector2D(bx, by)
    return sensors


directions_for_matrix = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def solution_one(sensors, y):
    visited = set()
    hashtags = set()

    def bfs(sensor, radius):
        queue = deque()
        queue.append((sensor.x, sensor.y, 0))

        while queue:
            x, y, level = queue.popleft()
            if level == 1:
                print('xy', (x, y))
            if y == 10:
                hashtags.add((x, y))
            for direction in directions_for_matrix:
                dx, dy = direction
                if level < radius and (x + dx, y + dy) not in visited:

                    queue.append((x + dx, y + dy, level + 1))

    for sensor in sensors:
        beacon = sensors[sensor]
        radius = (sensor - beacon).get_radius()
        bfs(sensor, radius)
        if beacon.to_tuple() in hashtags:
            hashtags.remove(beacon.to_tuple())
            print('aaaa')
        if sensor.to_tuple() in hashtags:
            hashtags.remove(sensor.to_tuple())

    print('Solution 1, ', len(hashtags))
    return len(hashtags)


sensor = Vector2D(8, 7)
beacon = Vector2D(2, 10)
print('Radius', (sensor - beacon).get_radius())

start_time = time.time()

sensors = parse_input(lines)
solution_one(sensors, 2_000_000)

end_time = time.time()


print('Time ellapsed', (end_time - start_time) * 1000)

file.close()
