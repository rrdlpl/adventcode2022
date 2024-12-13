from collections import defaultdict
from functools import cache
import re
import time

def parse_input():
  file = open('2024/day13/input.txt', 'r')
  lines = file.readlines()

  button_a = []
  button_b = []
  prizes = []


  for i in range(0,len(lines),4):
    matches = re.findall(r'[XY]\+(\d+)', lines[i])
    button_a.append(tuple(map(int, matches)))

    matches = re.findall(r'[XY]\+(\d+)', lines[i+1])
    button_b.append(tuple(map(int, matches)))

    matches = re.findall(r'(\d+)', lines[i+2])
    prizes.append(tuple(map(int, matches)))
  
  return button_a, button_b, prizes
  
# print(button_a)
# print(button_b)
# print(prizes)

def part_one():
  buttons_a, buttons_b, prizes = parse_input()
  cache = defaultdict(lambda: float('inf'))
    
  def dfs(a, b, prize_location, apress, bpress) -> bool:
    key = (prize_location, apress, bpress)
    px, py = prize_location
    if key in cache:
      return cache[key]
    if prize_location == (0, 0):
      return 0
    if px < 0 or py < 0 or apress > 100 or bpress > 100:
      return float('inf')
    ax, ay = a
    bx, by = b
    result = min(3 + dfs(a, b, (px - ax, py - ay), 1 + apress, bpress), 1 + dfs(a, b, (px - bx, py - by), apress, 1 + bpress))
    cache[key] = result
    return result

  result = 0
  for i in range(len(buttons_a)):
    print('Solving', i , ' / ', len(buttons_a))
    tokens = dfs(buttons_a[i], buttons_b[i], prizes[i], 0, 0)  
    if tokens != float('inf'):
      result += tokens
  return result
  
  


print('Solution 1.', part_one())


