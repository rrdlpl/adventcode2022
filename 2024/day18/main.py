from collections import defaultdict, deque


def parse_input(n, fallen_bytes_size=12):
  file = open('2024/day18/input.txt', 'r')
  lines = file.readlines()
  
  grid = []

  for i in range(n + 1):
    row = list('.' * (n + 1))
    grid.append(row)

  for i in range(0, fallen_bytes_size - 1):
    line = lines[i].strip().split(',')
    row, col = int(line[0]), int(line[1])
    grid[col][row] = '#'

  return grid


def render_grid(grid):
  for row in grid:
    print(''.join([str(cell) for cell in row]))



def part_one():  
  grid = parse_input(70, 1025)
  n = len(grid)
  render_grid(grid)
  def can_move(row, col):
    return 0 <= row < n and 0 <= col < n and grid[row][col] == '.'
  def bfs():
    queue = deque([])
    queue.append((0, 0, 0))
    visited = defaultdict(lambda: float('infinity'))
    visited[(0, 0)] = 0
  
    while queue:
      row, col, steps = queue.popleft()
      for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        next_row, next_col = row + dr, col + dc
        if not can_move(next_row, next_col): 
          continue
        if visited[(next_row, next_col)] > steps + 1:
            queue.append((next_row, next_col, steps + 1))
            visited[(next_row, next_col)] = steps + 1
    # print(visited)
    # for i, j in visited:
    #   grid[i][j] = 'O'
    # render_grid(grid)
    return visited[(n - 1, n - 1)]
    
  return bfs()
        

print('Solution 1', part_one())