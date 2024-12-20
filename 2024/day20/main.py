from collections import defaultdict, deque


def parse_input():
  file = open('2024/day20/input.txt', 'r')
  lines = file.readlines()
  grid = []
  for i in range(0, len(lines)):
    line = list(lines[i].strip())
    grid.append(line)
  return grid


def init(grid):
  start_position = None
  end_position = None
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == 'S':
        start_position = (i, j)
      elif grid[i][j] == 'E':
        end_position = (i, j)
  return start_position, end_position

def render_grid(grid):
  for row in grid:
    print(''.join(row))
    
def can_move(row, col, grid):
    return 0 <= row < len(grid) and 0 <= col < len(grid) and grid[row][col] != '#'


def bfs(grid, start, end, cheated_walls=None):
    queue = deque([])
    sr, sc = start
    queue.append((sr, sc, 0))
    visited = defaultdict(lambda: float('infinity'))
    visited[(sr, sc)] = 0
   
    while queue:
      row, col, steps = queue.popleft()
     
      for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        next_row, next_col = row + dr, col + dc
        if not can_move(next_row, next_col, grid ): 
          continue
        if visited[(next_row, next_col)] > steps + 1:
            queue.append((next_row, next_col, steps + 1))
            visited[(next_row, next_col)] = steps + 1
    return visited

def part_one():  
  return solve(2)

      
def part_two():
  return solve(20)

def solve(max_manhattan_distance):
    grid = parse_input()
    start, end = init(grid)
    distances = bfs(grid, start, end)
    saved_time_with_cheats = {}
    for row, col in distances:
      for dr in range(-max_manhattan_distance, max_manhattan_distance + 1, 1):
        for dc in range(-max_manhattan_distance, max_manhattan_distance + 1, 1):
          if abs(dr) + abs(dc) <= max_manhattan_distance:
            new_row, new_col = row + dr, col + dc
            if (new_row, new_col) in distances:
                if distances[(row, col)] > distances[(new_row, new_col)]:
                  time_saved =  distances[(row,col)] - distances[(new_row, new_col)] - abs(dr) - abs(dc) 
                  if time_saved > 0:
                      saved_time_with_cheats[((row, col),(new_row, new_col))] = time_saved
 
    count = 0
    for key in saved_time_with_cheats:
      if saved_time_with_cheats[key] >= 100:
        count += 1 

    return count


print('Solution 1. ', part_one())
print('Solution 2. ', part_two())