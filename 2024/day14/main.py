
from dataclasses import dataclass
import re
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
       
       robots.append(Robot(position, velocity))

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


# def part_two():
#  WIDE = 101
#  TALL = 103
#  grid = [['.' for _ in range(WIDE)] for _ in range(TALL)]
#  lines = []
#  robots = set(parse_input())

#  for row in range(TALL):
#    for col in range(WIDE):
#      if row == 0 or row == TALL - 1 or col == 0 or col == WIDE - 1:
#        grid[row][col] = '#'
#        lines.append((row, col))
  
print('Solution 1', part_one())

# pt. 1 first attempt 55301400