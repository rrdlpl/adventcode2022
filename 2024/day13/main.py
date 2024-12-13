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
    # print('Solving', i , ' / ', len(buttons_a))
    tokens = dfs(buttons_a[i], buttons_b[i], prizes[i], 0, 0)  
    if tokens != float('inf'):
      result += tokens
  return result
  

def part_two():
  def calc_a(a, b, p):
    ax, ay = a
    bx, by = b
    px, py = p
    return (by * px - bx * py) / (by * ax - bx * ay)
  
  def calc_b(ac, a, b, p):
    _, ay = a
    _, by = b
    _, py = p
    num = py - ay * ac
    # denom = bx * (by * ax - bx * ay)
    return num / by
  
  buttons_a, buttons_b, prizes = parse_input()
  tokens = 0
  tokens_partone_check = 0
  offset = 10000000000000
  for i in range(len(buttons_a)):
    a = buttons_a[i]
    b = buttons_b[i]
    p = (prizes[i][0] , prizes[i][1])

    a_press = calc_a(a, b, p)
    b_press = calc_b(a_press,a, b, p)
    
    p_offset = (prizes[i][0] + offset, prizes[i][1] + offset)    
    a_press_offset = calc_a(a, b, p_offset)
    b_press_offset = calc_b(a_press_offset, a, b, p_offset)
    
    if a_press.is_integer() and b_press.is_integer() and a_press >= 0 and b_press >= 0 and a_press <= 100 and b_press <= 100:
      tokens_partone_check += (a_press * 3) + b_press
      
    if a_press_offset.is_integer() and b_press_offset.is_integer() and a_press_offset >= 0 and b_press_offset >= 0:
      tokens += (a_press_offset * 3) + b_press_offset
  
  print('Part one check: ', tokens_partone_check)
  return tokens
    
  


print('Solution 1.', part_one())
print('Solution 2.', part_two())


