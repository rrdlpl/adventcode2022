file = open('day20/input.txt', 'r')
lines = file.readlines()


class Node:
    def __init__(self, value, index) -> None:
        self.left = None
        self.right = None
        self.value = value
        self.index = index


def parse_input(lines, key):
    original = []
    for i, line in enumerate(lines):
        line = line.strip()
        value = int(line)
        original.append(Node(value * key, i))

    original[0].left = original[len(original) - 1]
    original[0].right = original[1]
    original[len(original) - 1].right = original[0]
    original[len(original) - 1].left = original[len(original) - 2]

    for i in range(1, len(original) - 1):
        original[i].left = original[i - 1]
        original[i].right = original[i + 1]

    return original


def part_one(original):
    nodes = original.copy()
    zero = None

    for i in range(len(nodes)):
        if nodes[i].value == 0:
            zero = nodes[i]
            continue
        swap(nodes, i)

    grove = 0
    for _ in range(3):
        for _ in range(1000):
            zero = zero.right
        grove += zero.value
    print('solution 1', grove)


def swap(original, i):
    node = original[i]

    if node.value == 0:
        return

    target = node
    if node.value < 0:

        for _ in range(-1 * node.value % (len(original) - 1)):
            target = target.left

        if target == node:
            return

        node.left.right = node.right
        node.right.left = node.left
        target.left.right = node
        node.left = target.left
        target.left = node
        node.right = target
    elif node.value > 0:
        for _ in range(node.value % (len(original) - 1)):
            target = target.right
        if target == node:
            return

        node.right.left = node.left
        node.left.right = node.right
        target.right.left = node
        node.right = target.right
        target.right = node
        node.left = target


original = parse_input(lines, 1)

part_one(original)


def part_two():
    original = parse_input(lines, 811589153)
    nodes = original.copy()
    zero = None

    for _ in range(10):
        for i in range(len(nodes)):
            if nodes[i].value == 0:
                zero = nodes[i]
                continue
            swap(nodes, i)

    grove = 0
    for _ in range(3):
        for _ in range(1000):
            zero = zero.right
        grove += zero.value
    print('solution 2', grove)


part_two()
