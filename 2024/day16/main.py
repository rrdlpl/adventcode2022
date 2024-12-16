

from collections import defaultdict, deque
import heapq


def parse_input():
  file = open('2024/day16/input.txt', 'r')
  lines = file.readlines()
  grid = [list(line.strip()) for line in lines]
  
  return grid

def render_grid(grid):
  for row in grid:
    print(''.join(row))

def init(grid):
  start_position = None
  end_position = None
  start_position = None
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == 'S':
        start_position = (i, j)
      elif grid[i][j] == 'E':
        end_position = (i, j)
  return start_position, end_position

def part_one():
  grid = parse_input()
  (start_row, start_column), (end_row, end_column) = init(grid)
  def can_move(row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != '#'

  directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
  scores = defaultdict(lambda: float('inf'))
  queue = []
  
  scores[(start_row, start_column, directions[0])] = 0
  heapq.heappush(queue,  (start_row, start_column, directions[0], 0))

  while queue:
    (row, col, current_direction, current_score) = heapq.heappop(queue)
    if scores[(row, col, current_direction)] < current_score:
      continue
    for next_direction in directions:
      if current_direction == next_direction:
          continue
      if scores[(row, col, next_direction)] > current_score + 1000:
          scores[(row, col, next_direction)] = current_score + 1000
          heapq.heappush(queue, ( row, col, next_direction, current_score + 1000))
    
    dr, dc = current_direction
    next_row, next_col = row + dr, col + dc
    if can_move(next_row, next_col) and scores[(next_row, next_col, current_direction)] > current_score + 1:
      scores[(next_row, next_col, current_direction)] = current_score + 1
      heapq.heappush(queue, ( next_row, next_col, current_direction, current_score + 1))

  result = float('infinity')

  for dir in directions:
    print(scores[(end_row, end_column, dir)])
    if (end_row, end_column, dir) in scores:
      result = min(result, scores[(end_row, end_column, dir)])
  return result, scores


def part_two():
  grid = parse_input()
  start, end = init(grid)
  min_score, _ = part_one()
  
  print('Solution 1', min_score)
  all_paths = set()
  scores = {(start, 0): 0}
  path = [(start, 0)]
  
  visited = set()
  visited.add(start)
  directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

  def can_move(row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != '#'

  def backtrack(current_score):
    current_node, current_direction = path[-1]
    if current_score == min_score and current_node == end:
      all_paths.update(visited)
    elif current_score > min_score:
      return

    row, col = current_node
    
    for next_direction, extra_score in [(current_direction, 0), ((current_direction + 1) % 4, 1000), ((current_direction - 1) % 4, 1000)]:
      dr, dc = directions[next_direction]
      next_row, next_column = row + dr, col + dc
      if can_move(next_row, next_column) and (next_row, next_column) not in visited:
          next_node = ((next_row, next_column), next_direction)
          new_score = current_score + extra_score + 1
          if next_node not in scores or new_score <= scores[next_node]:
              scores[next_node] = new_score
              visited.add((next_row, next_column))
              path.append(next_node)
              backtrack(new_score)
              visited.remove((next_row, next_column))
              path.pop()

  backtrack(0)
  return len(all_paths)


  


print('SOlutino 2', part_two())