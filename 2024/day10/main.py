import time
file = open('2024/day10/input.txt', 'r')
lines = file.readlines()

grid = [list(line.strip()) for line in lines ]
for i in range(len(grid)):
  for j in range(len(grid[0])):
    if grid[i][j] == '.':
      continue
    grid[i][j] = int(grid[i][j])


def part_one():
  visited = set()
  directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
  
  result = 0
  def dfs(x, y):
    visited.add((x, y))
    
    if grid[x][y] == 9:
      nonlocal result
      result += 1
      
    for dx, dy in directions:
      new_x, new_y = x + dy, y + dx
      if (new_x, new_y) in visited:
        continue
      if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == grid[x][y] + 1:
        dfs(new_x, new_y)
  
  total = 0
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == 0:
        visited = set()
        result = 0
        dfs(i, j)
        total += result
        
  return total 


def part_two():
  visited = set()
  directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
  
  result = 0
  def dfs(x, y):
    visited.add((x, y))
    
    if grid[x][y] == 9:
      nonlocal result
      result += 1
      
    for dx, dy in directions:
      new_x, new_y = x + dy, y + dx
      # if (new_x, new_y) in visited:
      #   continue
      if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == grid[x][y] + 1:
        dfs(new_x, new_y)
  
  total = 0
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == 0:
        visited = set()
        result = 0
        dfs(i, j)
        total += result
        
  return total 


print('Solution 1.', part_one())
print('Solution 2.', part_two())