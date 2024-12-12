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
  
  for i in range(m):
    for j in range(n):
      if (i, j) not in visited:
        region = set()
        dfs(i, j, grid[i][j], region)
        regions.append((grid[i][j], region))

  
  print('Regions: ')
  print(regions)
  
  perimeters = 0
  for plant, region in regions:
    perimeters += calculate_perimeter(region) * len(region)
  return perimeters 
  
 
# 62
# 9387

print('Solution 1.', part_one())