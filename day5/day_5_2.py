

from collections import deque
import re


file = open('day5/input.txt', 'r')
lines = file.readlines()

stacks = [
    deque(['B', 'L', 'D', 'T', 'W', 'C', 'F', 'M']),
    deque(['N', 'B', 'L']),
    deque(['J', 'C', 'H', 'T', 'L', 'V']),
    deque(['S', 'P', 'J', 'W']),
    deque(['Z', 'S', 'C', 'F', 'T', 'L', 'R']),
    deque(['W', 'D', 'G', 'B', 'H', 'N', 'Z']),
    deque(['F', 'M', 'S', 'P', 'V', 'G', 'C', 'N']),
    deque(['W', 'Q', 'R', 'J', 'F', 'V', 'C', 'Z']),
    deque(['R', 'P', 'M', 'L', 'H'])
]

for line in lines:
    move, fr, to = [int(s) for s in re.findall(r'\b\d+\b', line)]
    fr -= 1
    to -= 1

    temp = []
    for i in range(move):
        p = stacks[fr].pop()
        temp.append(p)

    for p in temp[::-1]:
        stacks[to].append(p)

result = []
for stack in stacks:
    result.append(stack.pop())

print(''.join(result))
