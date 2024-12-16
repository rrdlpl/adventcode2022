
from collections import defaultdict
from dataclasses import dataclass
import os
import re
import time
from typing import Tuple


@dataclass
class Robot:
  position: Tuple[int, int]
  velocity: Tuple[int, int]

def parse_input():
   file = open('2024/day14/input.txt', 'r')
   lines = file.readlines()
   robots = []
   for line in lines:
     line = line.strip()
     match = re.search("p=(\\d+,\\d+) v=(-?\\d+,-?\\d+)", line)
     if match:
       position = tuple(map(int, match.group(1).split(',')))
       velocity = tuple(map(int, match.group(2).split(',')))
        
       robots.append(Robot(position, position, velocity))

   return robots


def part_one():
  robots = parse_input()
  seconds = 100 
  WIDE = 101
  TALL = 103
  
  center = (WIDE // 2, TALL // 2)
  quadrants = [0, 0, 0, 0]
  def get_quadrant(position):
    x, y = position
    if x > center[0] and y > center[1]:
        return 0
    elif x < center[0] and y > center[1]:
        return 1
    elif x < center[0] and y < center[1]:
        return 2
    elif x > center[0] and y < center[1]:
        return 3
    return -1

  for robot in robots:
    position = robot.position

    vx = robot.velocity[0]
    vy = robot.velocity[1]
    new_velocity = (vx * seconds, vy * seconds)
    new_position = ((position[0] +  new_velocity[0]) % WIDE , (position[1] + new_velocity[1]) % TALL)
    robot.position = new_position
    
  
  for robot in robots:
    q_index = get_quadrant(robot.position)
    if q_index == -1:
      continue
    quadrants[q_index] += 1

  result = 1
  for q in quadrants:
    result *= q
  return result


def part_two():
 # which is 101 tiles wide and 103 tiles tall
 WIDE = 101
 TALL = 103
 def move_robot(robots, seconds):
    for robot in robots:
      position = robot.position
      vx = robot.velocity[0]
      vy = robot.velocity[1]
      new_velocity = (vx * seconds, vy * seconds)
      new_position = ((position[0] +  new_velocity[0]) % WIDE , (position[1] + new_velocity[1]) % TALL)
      robot.position = new_position


 def print_grid(robots):
  robot_set = set()
  grid = [[' ' for _ in range(WIDE)] for _ in range(TALL)]
  # print('tall', len(grid))
  # print('wide', len(grid[0]))
  for robot in robots:
    robot_set.add(robot.position)
  
  for row in range(len(grid)):
     for col in range(len(grid[0])):
       if (row, col) in robot_set:
         grid[row][col] = '#'
    #  print(''.join(grid[row]))
  return grid
 
 robots = parse_input() 
 
 def contains_tree(grid):
   for row in grid:
     if '#################' in ''.join(row):
       print('aAASDFASDFASdf')
       return True
   return False
 
  # def calculate_cycle(robots):
  #   grid = print_grid(robots)
  #   cycle = defaultdict(lambda: 0)
  #   for i in range(1, 10000, 1):
      
  #     grid = print_grid(robots)
  #     move_robot(robots, i)
  #     key = ' '.join(''.join(row) for row in grid)
  #     if key in cycle:
  #       print('Cycle found', i)
  #       print('Previous ', cycle[key])
  #       print('Cycle offset', i - cycle[key])
  #       return 
  #     cycle[key] = i

#  calculate_cycle(robots)
       

 with open("output2.txt", mode="w", encoding="UTF-8") as output:
  for i in range(0, 10000, 1):
    grid = print_grid(robots)
    move_robot(robots, 1)
    if contains_tree(grid):
      output.write('Iteration '+ str(i) + '\n\n')
      output.write('\n'.join([''.join(row) for row in grid]))
      output.write('\n\n')
      return i
  
  
print('Solution 1', part_one())

print('Solution 2', part_two())

# pt. 1 first attempt 55301400

# pt.  2 2141 
# 2142
# 2143

# 6494
# 6495