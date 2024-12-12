from collections import defaultdict
import time
file = open('2024/day12/input.txt', 'r')
lines = file.readlines()

grid = [line.strip() for line in lines]
m = len(grid)
n = len(grid[0])
def part_one():
  def calculate_perimeter(region):
    perimeter = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for x, y in region:
        for dx, dy in directions:
            neighbor = (x + dx, y + dy)
            if neighbor not in region:
                perimeter += 1
    return perimeter

  def dfs(i, j, plant, region):
    visited.add((i, j))
    region.add((i, j))
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
      new_x, new_y = i + dx, j + dy
      if (new_x, new_y) in visited:
        continue
      if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == plant:
        dfs(new_x, new_y, plant,region)

  visited = set()
  
  regions = []
  
  for x in range(m):
    for y in range(n):
      if (x, y) not in visited:
        region = set()
        dfs(x, y, grid[x][y], region)
        regions.append((grid[x][y], region))

  
  print('Regions: ')
  print(regions)
  
  perimeters = 0
  for plant, region in regions:
    perimeters += calculate_perimeter(region) * len(region)
  return perimeters 

def part_two():
  def count_sides(region):
    top, right, bottom, left = set(), set(), set(), set()

    for x, y in region:
        if (x - 1, y) not in region: top.add((x, y))
        if (x, y + 1) not in region: right.add((x, y))
        if (x + 1, y) not in region: bottom.add((x, y))
        if (x, y - 1) not in region: left.add((x, y))

    sides = 0
    for (x, y) in top:
        if (x, y) in right:
            sides += 1
        elif (x - 1, y + 1) in left:
            sides += 1
        if (x, y) in left:
            sides += 1
        elif (x - 1, y - 1) in right:
            sides += 1

    for (x, y) in bottom:
        if (x, y) in left:
            sides += 1
        elif (x + 1, y - 1) in right:
            sides += 1
        if (x, y) in right:
            sides += 1
        elif (x + 1, y + 1) in left:
            sides += 1

    return sides

  def dfs(i, j, plant, region):
    visited.add((i, j))
    region.add((i, j))

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
      new_x, new_y = i + dx, j + dy
      if (new_x, new_y) in visited:
        continue
      if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == plant:
        dfs(new_x, new_y, plant,region)

  visited = set()
  regions = []  
  for x in range(m):
    for y in range(n):
      if (x, y) not in visited:
        region = set()
        dfs(x, y, grid[x][y], region)
        regions.append((grid[x][y], region))

  
  print('Regions: ')
  print(regions)
  
  sides = 0
  for plant, region in regions:
    sides += count_sides(region) * len(region)
  return sides 
  
 
# print('Solution 1.', part_one())

print('Solution 2.', part_two())