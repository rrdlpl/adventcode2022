from collections import defaultdict, deque
from copy import copy
from itertools import combinations


import re
import time


class Valve:
    def __init__(self, name, rate, tunnels) -> None:
        self.rate = rate
        self.tunnels = tunnels
        self.name = name

    def bfs(self):
        queue = deque()
        queue.append((self, 0, self.rate))
        visited = set()
        visited.add(self.name)
        path = {}

        while queue:
            node, level = queue.popleft()
            visited.add(node.name)
            for v in node.next_valves:
                if not v.name in visited:
                    queue.append((v, level + 1, v.rate))
                    path[v.name] = (node.name, level + 1, v.rate, v.is_open)
        print(path)

    def print_all(self):
        print('Valve ', self.name, ' rate=', self.rate,
              ';', 'Next valves', self.next_valves)


file = open('day16/input.txt', 'r')
lines = file.readlines()

start_time = time.time()


def parse_input(lines):
    valves = {}

    for line in lines:
        line = line.strip()
        line = line.split(';')

        rate = [int(s) for s in re.findall(r'-?\d+', line[0])][0]
        name = line[0].split()[1]

        tunnels = [t.strip() for t in line[1].replace(' tunnel leads to ', '').replace(
            ' tunnels lead to ', '').replace('valves ', '').replace('valve ', '').split(',')
        ]

        valves[name] = Valve(name, rate, tunnels)
    # print(valves)
    return valves


def part_one(valves):
    cache = {}

    def backtrack(source, minutes, opened_valves):
        if minutes <= 0:
            return 0

        max_flow = 0

        set_key = ''.join(sorted(list(opened_valves)))

        if (source, minutes, set_key) in cache:
            return cache[(source, minutes, set_key)]

        if source in opened_valves:
            for next_valve in valves[source].tunnels:
                max_flow = max(max_flow,
                               backtrack(next_valve, minutes - 1, opened_valves))
        else:

            current_flow = valves[source].rate * (minutes - 1)

            for next_valve in valves[source].tunnels:
                if current_flow > 0:
                    opened_valves.add(source)
                    max_flow = max(max_flow, current_flow +
                                   backtrack(next_valve, minutes - 2, opened_valves))
                    opened_valves.remove(source)

                max_flow = max(max_flow, backtrack(
                    next_valve, minutes - 1, opened_valves))

        cache[(source, minutes, set_key)] = max_flow

        return max_flow

    return backtrack('AA', 30, set())


# def part_two(valves, distances):
#     cache = {}

#     def backtrack(source, elefant, minutes, opened_valves):
#         if minutes <= 0:
#             return 0

#         max_flow = 0

#         set_key = ''.join(sorted(list(opened_valves)))

#         if (source, minutes, set_key) in cache:
#             return cache[(source, minutes, set_key)]

#         if source in opened_valves:
#             for next_valve in valves[source].tunnels:
#                 max_flow = max(max_flow,
#                                backtrack(next_valve, minutes - 1, opened_valves))
#         else:

#             current_flow = valves[source].rate * (minutes - 1)

#             for next_valve in valves[source].tunnels:
#                 if current_flow > 0:
#                     opened_valves.add(source)
#                     max_flow = max(max_flow, current_flow +
#                                    backtrack(next_valve, minutes - 2, opened_valves))
#                     opened_valves.remove(source)

#                 max_flow = max(max_flow, backtrack(
#                     next_valve, minutes - 1, opened_valves))

#         cache[(source, minutes, set_key)] = max_flow

#         return max_flow

#     return backtrack('AA', 'AA', 30,  set())


valves = parse_input(lines)
max_flow = part_one(valves)
print('Solution 1', max_flow)


print('Solution 2', max_flow)


# print('Solution 2', max_flow)

end_time = time.time()
print('Time ellapsed', (end_time - start_time) * 1000)

file.close()
