

from collections import defaultdict, deque
import re
import operator


def parse_input(lines):
    blueprints = {}
    for line in lines:
        line = line.strip()
        costs = re.findall(r'\d+', line)
        id = int(costs[0])
        robot_costs = {
            # ore, clay, obsidian, geode
            'ore':  (int(costs[1]), 0, 0, 0),
            'clay': (int(costs[2]), 0, 0, 0),
            'obsidian': (int(costs[3]), int(costs[4]), 0, 0),
            'geode': (int(costs[5]), 0, int(costs[6]), 0)
        }
        blueprints[id] = robot_costs

    return blueprints


def can_build_robot(blueprint, robot_type, resources):
    robot_cost = blueprint[robot_type]
    req_ore, req_clay, req_obsidian,  _ = robot_cost
    ore, clay, obsidian, _ = resources
    if robot_type == 'ore' or robot_type == 'clay':
        return ore >= req_ore

    if robot_type == 'obsidian':
        return ore >= req_ore and clay >= req_clay

    return ore >= req_ore and obsidian >= req_obsidian


def build_robot(blueprint, robot_type, resources):
    robot_cost = blueprint[robot_type]
    return tuple(map(operator.sub, resources, robot_cost))


def add_robot(robots: tuple, robot_type):
    _map = {
        'ore': (1, 0, 0, 0),
        'clay': (0, 1, 0, 0),
        'obsidian': (0, 0, 1, 0),
        'geode': (0, 0, 0, 1)
    }
    robot = _map[robot_type]

    return tuple(map(operator.add, robots, robot))


def collect_minerals(resources, robots):
    return tuple(map(operator.add, resources, robots))


def get_max_costs(blueprint):
    max_ore = max_clay = max_obsidian = -1
    for robot_type in blueprint:
        robot_cost = blueprint[robot_type]
        ore, clay, obsidian, _ = robot_cost
        max_ore = max(max_ore, ore)
        max_clay = max(max_clay, clay)
        max_obsidian = max(max_obsidian, obsidian)

    return {
        'ore': max_ore,
        'clay': max_clay,
        'obsidian': obsidian
    }


def part_one(blueprints):
    time = 32
    initial_resources = (0, 0, 0, 0)
    initial_robots = (1, 0, 0, 0)

    geode = None
    quality_level = 0

    part_two = 1
    for id in blueprints:
        if id <= 3:
            part_two *= get_max_geode(32, initial_resources,
                                      initial_robots, blueprints[id])
            print('blueprint', id, part_two)

        part_one = get_max_geode(
            24, initial_resources, initial_robots, blueprints[id])
        quality_level += part_one * id

    print('Solution one', part_one)
    print('Solution two', part_two)
    return quality_level


def get_max_geode(time_left, initial_resources, initial_robots, blueprint):
    queue = deque()
    visited = set()

    max_geodes = 0
    max_robots = get_max_costs(blueprint)

    queue.append((initial_resources, initial_robots, time_left))

    while queue:
        resources, robots, time_left = queue.popleft()
        ore_robots, clay_robots, obsidian_robots, geode_robots = robots

        robot_map = {
            'ore': ore_robots,
            'clay': clay_robots,
            'obsidian': obsidian_robots
        }
        _, _, _, geodes = resources

        visited.add(robots)

        if time_left == 1:
            max_geodes = max(max_geodes, geodes + geode_robots * time_left)
            continue

        max_geodes = max(max_geodes, geodes + geode_robots * time_left)

        if obsidian_robots > 0 and can_build_robot(blueprint, 'geode', resources):
            next_resources = build_robot(blueprint, 'geode', resources)

            next_resources = collect_minerals(next_resources, robots)
            next_robots = add_robot(robots, 'geode')

            if next_robots not in visited:
                queue.append((next_resources, next_robots, time_left - 1))
            continue

        for robot_type in ['obsidian', 'clay', 'ore']:
            if robot_map[robot_type] < max_robots[robot_type] and can_build_robot(blueprint, robot_type, resources):
                next_resources = build_robot(blueprint, robot_type, resources)
                next_resources = collect_minerals(next_resources, robots)
                next_robots = add_robot(robots, robot_type)
                if next_robots not in visited:
                    queue.append((next_resources, next_robots, time_left - 1))

        next_resources = collect_minerals(resources, robots)
        queue.append((next_resources, robots, time_left - 1))

    return max_geodes


file = open('day19/input.txt', 'r')
lines = file.readlines()


blueprints = parse_input(lines)

print('max costs', get_max_costs(blueprints[2]))
print('Solution 1', part_one(blueprints))
