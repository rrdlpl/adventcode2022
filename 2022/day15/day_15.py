
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

    for sensor in sensors:
        beacon = sensors[sensor]
        set_ranges(sensor, beacon, ranges_without_beacon, target_y)

    first_left, first_right = ranges_without_beacon[target_y][0]
    interv = interval(min(first_left.x, first_right.x),
                      max(first_left.x, first_right.x))

    for i in range(1, len(ranges_without_beacon[target_y])):
        left, right = ranges_without_beacon[target_y][i]
        min_x = min(left.x, right.x)
        max_x = max(left.x, right.x)
        interv = interv | interval[min_x, max_x]

    # print('Interval', interv)
    # print('Solution 1.', interv)
    return interv


def set_ranges(sensor, beacon, ranges_without_beacon, target_y):
    radius = (sensor - beacon).get_radius()
    x = sensor.x

    if (sensor.y < target_y and sensor.y + radius < target_y) or (sensor.y > target_y and sensor.y - radius > target_y):
        return

    dy = abs(target_y - sensor.y)

    left = Vector2D(x - radius + dy, target_y)
    right = Vector2D(x + radius - dy, target_y)

    adjust_overlapping_range(target_y, ranges_without_beacon, left, right)


def set_ranges_2(sensor, beacon, ranges_without_beacon, target_y, low, high):
    radius = (sensor - beacon).get_radius()
    x = sensor.x

    if (sensor.y < target_y and sensor.y + radius < target_y) or (sensor.y > target_y and sensor.y - radius > target_y):
        return

    dy = abs(target_y - sensor.y)

    left = Vector2D(max(x - radius + dy, low), target_y)
    right = Vector2D(min(x + radius - dy, high), target_y)

    adjust_overlapping_range(target_y, ranges_without_beacon, left, right)


def adjust_overlapping_range(y, ranges_without_beacon, left, right):
    if y in ranges_without_beacon:
        ranges_without_beacon[y].append((left, right))
    else:
        ranges_without_beacon[y] = [(left, right)]


def solution_two(sensors, target_y, ranges_without_beacon, low, high):

    for sensor in sensors:
        beacon = sensors[sensor]
        set_ranges_2(sensor, beacon, ranges_without_beacon,
                     target_y, low, high)

    # print('Interval', interv)
    # print('Solution 1.', interv)
    return ranges_without_beacon


def get_tunning_freq(sensors):
    ranges_without_beacon = {}

    intervals = []

    high = 4_000_000
    low = 0
    for target_y in range(high):
        ranges_without_beacon = solution_two(
            sensors, target_y, ranges_without_beacon, low, high)

        interv = interval()
        print('target y', target_y)
        for left, right in ranges_without_beacon[target_y]:
            interv = interv | interval([left.x, right.x])

        print('Interval', interv)
        intervals.append(interv)

    for y, interv in enumerate(intervals):
        if interv == interval([low, high]):

            continue
        _, x2 = interv[0]
        for k in range(1, len(interv)):
            x3, _ = interv[k]
            if x3 - x2 >= 2:
                print('Found gap at', interv, ' x = ', x2,
                      'Freq = ',  (x2 + 1) * 4_000_000 + y)
                return

        print('Found gap at', y, interv, )


start_time = time.time()
sensors = parse_input(lines)
# interv = solution_one(sensors, 10)
# print('Solution 1', interv)

get_tunning_freq(sensors)

end_time = time.time()


print('Time ellapsed', (end_time - start_time) * 1000)

file.close()
