from collections import defaultdict, deque


def parse_input(n ):
  file = open('2024/day18/input.txt', 'r')
  lines = file.readlines()
  grid = []

  for i in range(n + 1):
    row = list('.' * (n + 1))
    grid.append(row)
  
  corrupted_memory = []
  for i in range(0, len(lines)):
    line = lines[i].strip().split(',')
    row, col = int(line[0]), int(line[1])
    # grid[col][row] = '#'
    corrupted_memory.append((row, col))

  return grid, corrupted_memory


def render_grid(grid):
  for row in grid:
    print(''.join([str(cell) for cell in row]))


def can_move(row, col, grid):
    return 0 <= row < len(grid) and 0 <= col < len(grid) and grid[row][col] == '.'
def bfs(grid):
    queue = deque([])
    queue.append((0, 0, 0))
    visited = defaultdict(lambda: float('infinity'))
    visited[(0, 0)] = 0
    n = len(grid)
  
    while queue:
      row, col, steps = queue.popleft()
      if row == n - 1 and col == n - 1:
        return steps
      for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        next_row, next_col = row + dr, col + dc
        
        if not can_move(next_row, next_col, grid): 
          continue
        if visited[(next_row, next_col)] > steps + 1:
            queue.append((next_row, next_col, steps + 1))
            visited[(next_row, next_col)] = steps + 1
    return visited[(n - 1, n - 1)]

def part_one():  
  grid, corrupted_memory = parse_input(70)
  for row, col in corrupted_memory[:1024]:
    grid[row][col] = '#'
  render_grid(grid)
  return bfs(grid)

def part_two():
  grid, corrupted_memory = parse_input(70)
  for row, col in corrupted_memory[:1024]:
    grid[row][col] = '#'
  
  for row, col in corrupted_memory[1024:]:
    grid[row][col] = '#'
    steps = bfs(grid)
    if steps == float('infinity'):
      print('Solution 2', (row, col))
      return
    

print('Solution 1', part_one())
print('Solution 2', part_two())