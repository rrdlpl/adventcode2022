from collections import defaultdict, deque
from copy import copy
from itertools import combinations


import re
import time


class Valve:
    def __init__(self, name, rate, tunnels, index) -> None:
        self.rate = rate
        self.tunnels = tunnels
        self.name = name
        self.index = index

    def print_all(self):
        print('Valve ', self.name, ' rate=', self.rate,
              ';', 'Next valves', self.tunnels, 'index=', self.index)


file = open('day16/input.txt', 'r')
lines = file.readlines()

start_time = time.time()


def parse_input(lines):
    valves = {}

    index = 0

    for line in lines:
        line = line.strip()
        line = line.split(';')

        rate = [int(s) for s in re.findall(r'-?\d+', line[0])][0]
        name = line[0].split()[1]

        tunnels = [t.strip() for t in line[1].replace(' tunnel leads to ', '').replace(
            ' tunnels lead to ', '').replace('valves ', '').replace('valve ', '').split(',')
        ]

        valves[name] = Valve(name, rate, tunnels, index)
        index += 1
    return valves


def part_one(valves):
    opened = [0] * len(valves)

    def bfs(source, opened_valves, time):
        queue = deque()
        queue.append((source, tuple(opened_valves), time, 0))
        max_flow = 0
        visited = set()

        for v in valves:
            if valves[v].rate == 0:
                opened[valves[v].index] = 1

        while queue:
            s, opened_valves, time_left, current_flow = queue.popleft()

            if time_left == 1:
                max_flow = max(max_flow, current_flow)
                continue

            opened_valves = list(opened_valves)
            max_flow = max(max_flow, current_flow)

            source_index = valves[s].index
            if opened_valves[source_index] == 1:
                current_opened_valves = tuple(opened_valves)

                for next_valve in valves[s].tunnels:
                    if (next_valve, current_opened_valves, current_flow) not in visited:
                        queue.append((next_valve, current_opened_valves,
                                     time_left - 1, current_flow))
                        visited.add(
                            (next_valve, current_opened_valves, current_flow))
                continue

            without_this_open = tuple(opened_valves)
            opened_valves[source_index] = 1
            with_this_open = tuple(opened_valves)
            new_flow = valves[s].rate * (time_left - 1)

            for next_valve in valves[s].tunnels:
                if (next_valve, without_this_open, current_flow) not in visited:
                    queue.append((next_valve, without_this_open,
                                  time_left - 1, current_flow))
                    visited.add((next_valve, without_this_open, current_flow))

                if new_flow > 0:
                    queue.append((next_valve, with_this_open,
                                  time_left - 2, current_flow + new_flow))

        return max_flow

    return bfs('AA', tuple(opened), 30)


valves = parse_input(lines)

for v in valves:
    valves[v].print_all()

max_flow = part_one(valves)
print('Solution 1', max_flow)


print('Solution 2', max_flow)


# print('Solution 2', max_flow)

end_time = time.time()
print('Time ellapsed', (end_time - start_time) * 1000)

file.close()
