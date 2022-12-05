

from collections import deque
import re


file = open('day5/input.txt', 'r')
lines = file.readlines()


result = 0

stacks = [deque(['B', 'L', 'D', 'T', 'W', 'C', 'F', 'M']),
          deque(['N', 'B', 'L']),
          deque(['J', 'C', 'H', 'T', 'L', 'V']),
          deque(['S', 'P', 'J', 'W']),
          deque(['Z', 'S', 'C', 'F', 'T', 'L', 'R']),
          deque(['W', 'D', 'G', 'B', 'H', 'N', 'Z']),
          deque(['F', 'M', 'S', 'P', 'V', 'G', 'C', 'N']),
          deque(['W', 'Q', 'R', 'J', 'F', 'V', 'C', 'Z']),
          deque(['R', 'P', 'M', 'L', 'H'])]

for line in lines:

    instruction = [int(s) for s in re.findall(r'\b\d+\b', line)]
    move = instruction[0]
    fr = instruction[1] - 1
    to = instruction[2] - 1

    for i in range(move):
        p = stacks[fr].pop()
        stacks[to].append(p)

result = []
for stack in stacks:

    result.append(stack.pop())

print(''.join(result))
