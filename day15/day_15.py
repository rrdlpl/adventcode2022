
import math
import re
import time
from interval import interval, imath

union = interval[1, 2] | interval[4, 5]
print(union)

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


def solution_one(sensors, target_y):
    ranges_without_beacon = {

    }

    sensors_at_y = []
    for sensor in sensors:
        beacon = sensors[sensor]
        set_ranges(sensor, beacon, ranges_without_beacon, target_y)
        if sensor.y == target_y:
            sensors_at_y.append(sensor)

    first_left, first_right = ranges_without_beacon[target_y][0]
    interv = interval(min(first_left.x, first_right.x),
                      max(first_left.x, first_right.x))

    for i in range(1, len(ranges_without_beacon[target_y])):
        left, right = ranges_without_beacon[target_y][i]

        min_x = min(left.x, right.x)
        max_x = max(left.x, right.x)

        interv = interv | interval[min_x, max_x]

    print('Interval', interv)
    print('Solution 1.', interv)


def set_ranges(sensor, beacon, ranges_without_beacon, target_y):
    radius = (sensor - beacon).get_radius()
    x = sensor.x

    if (sensor.y < target_y and sensor.y + radius < target_y) or (sensor.y > target_y and sensor.y - radius > target_y):
        return

    dy = abs(target_y - sensor.y)
    print('Radius ', radius)
    print('Sensor => ', sensor, 'dy', dy)
    left = Vector2D(x - radius + dy, target_y)
    right = Vector2D(x + radius - dy, target_y)
    print('  adding left', left)
    print('  adding right', right)
    adjust_overlapping_range(target_y, ranges_without_beacon, left, right)


def adjust_overlapping_range(y, ranges_without_beacon, left, right):
    if y in ranges_without_beacon:
        ranges_without_beacon[y].append((left, right))
    else:
        ranges_without_beacon[y] = [(left, right)]


start_time = time.time()
sensors = parse_input(lines)
solution_one(sensors, 2_000_000)

end_time = time.time()


print('Time ellapsed', (end_time - start_time) * 1000)

file.close()
