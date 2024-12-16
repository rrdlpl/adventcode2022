

from collections import deque


def parse_input():
  file = open('2024/day15/input_a.txt', 'r')
  instructions = open('2024/day15/instructions.txt', 'r')
  lines = file.readlines()
  grid = [list(line.strip()) for line in lines]
  
  return [grid, ''.join([line.strip() for line in instructions.readlines()])]

def init(grid):
  walls = set()
  boxes = set()
  start_position = None
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == '#':
        walls.add((i, j))
      elif grid[i][j] == '@':
        start_position = (i, j)
      elif grid[i][j] == 'O':
        boxes.add((i, j))
  return start_position, boxes, walls

def render_grid(grid):
  for row in grid:
    print(''.join(row))
  

def move(instruction):
  m = {
    '<': (-1, 0),
    '^': (0, -1),
    '>': (1, 0),
    'v': (0, 1),
  }
  return m[instruction]

def part_one():
  grid, instructions = parse_input()
  current_position, boxes, walls = init(grid)
  render_grid(grid)
  for instruction in instructions:
    dx, dy = move(instruction)
    print("Move: ", instruction, "\n")
    new_position = (current_position[0] + dy, current_position[1] + dx)
    
    if new_position in walls:
      render_grid(grid)
      print("")
      continue
    
    if new_position in boxes:
       empty_box = new_position
       can_move = False
       while empty_box in boxes:
         if grid[empty_box[0] + dy][empty_box[1] + dx] == '.':
           empty_box = (empty_box[0] + dy, empty_box[1] + dx)
           can_move = True
           break
         if (empty_box[0] + dy, empty_box[1] + dx) in walls:
           can_move = False
           break
         empty_box = (empty_box[0] + dy, empty_box[1] + dx)
       if can_move:
         grid[current_position[0]][current_position[1]] = '.'
         boxes.remove(new_position)
         boxes.add(empty_box)
         current_position = new_position
         grid[current_position[0]][current_position[1]] = '@'
         grid[empty_box[0]][empty_box[1]] = 'O'
         
    else:
       grid[current_position[0]][current_position[1]] = '.'
       grid[new_position[0]][new_position[1]] = '@'
       current_position = new_position
    
    
    # render_grid(grid)
    # print("")
  
  answer  = 0
  for i, j in boxes:
    answer += (i*100) + j
  return answer


def resize_map(grid):
  map = []
  for i in range(len(grid)):
    new_row = []
    for j in range(len(grid[0])):
      
      tile = grid[i][j]
      if tile == '.':
        new_row.append('.')
        new_row.append('.')
      if tile == '#':
        new_row.append('#')
        new_row.append('#')
      if tile == '@':
        new_row.append('@')
        new_row.append('.')
      if tile == 'O':
        new_row.append('[')
        new_row.append(']')
    map.append(new_row)
  return map
      
def init_2(map):
  for i in range(len(map)):
    for j in range(len(map[0])):
      if map[i][j] == '@':
        return (i, j)
  return None

def move_boxes_horizontally(map, current_position, direction):
    dx, dy = direction
    row, col = current_position
    new_row, new_col, = row + dy, col + dx
    last_col = new_col
          
    while map[row][last_col] != '.' and map[row][last_col] != '#':
      last_col += dx
    if map[row][last_col] == '#':
        return current_position
    shift_cols = last_col
    while shift_cols != col - dx:
        map[row][shift_cols] = map[row][shift_cols - dx]
        shift_cols -= dx
    map[row][col] = '.'
    col = new_col
    
    current_position = (new_row, new_col)
      
    return current_position

def move_boxes_vertically(map, current_position, direction):
  row, col = current_position
  dx, dy = direction
  new_row, new_col = row + dy, col + dx
  queue = deque()
  queue.append((row, col))
  boxes_to_move = {}
  boxes_to_move[(new_row, new_col)] = map[new_row][new_col]
  while queue:
      current_row, current_col = queue.popleft()
      nr, nc = current_row + dy, current_col + dx
      if map[nr][nc] == '#':
          return current_position
      if map[nr][nc] == '.':
          continue
      boxes_to_move[(nr, nc)] = map[nr][nc]
      if map[nr][nc] == '[':
          queue.append((nr, nc))
          queue.append((nr, nc + 1))
          boxes_to_move[(nr, nc + 1)] = map[nr][nc + 1]
      elif map[nr][nc] == ']':
          queue.append((nr, nc))
          queue.append((nr, nc - 1))
          boxes_to_move[(nr, nc - 1)] = map[nr][nc - 1]
   

  
  if boxes_to_move:
      for ((i, j), _) in boxes_to_move.items():
          map[i][j] = '.'
      for ((i, j), tile) in boxes_to_move.items():
          map[i + dy][j + dx] = tile

      map[row][col] = '.'
      map[new_row][col] = '@'
      current_position = (new_row, new_col)
  # print('Current position',   current_position)
  return current_position

def part_two():
  grid, instructions = parse_input()
  map = resize_map(grid)
  current_position = init_2(map)
  render_grid(map)

  for instruction in instructions:
    dx, dy = move(instruction)
    # print("Move: ", instruction, "\n", current_position)
    
    next_position = (current_position[0] + dy, current_position[1] + dx)
    
    if map[next_position[0]][next_position[1]] == '#':
      # render_grid(map)
      continue
    if map[next_position[0]][next_position[1]] == '.':
      map[current_position[0]][current_position[1]] = '.'
      map[next_position[0]][next_position[1]] = '@'
      current_position = next_position
      # render_grid(map)
      continue
    if instruction == '>' or instruction == '<':
      current_position = move_boxes_horizontally(map, current_position, (dx, dy))
      if current_position == None: 
        print('alert hori', current_position )
      # render_grid(map)
      continue
    if instruction == 'v' or instruction == '^':
      current_position = move_boxes_vertically(map, current_position, (dx, dy))
      if current_position == None: 
        print('alert vert', current_position )
      # render_grid(map)
      continue

  answer = 0
  for i in range(len(map)):
    for j in range(len(map[0])):
      if map[i][j] == '[':
        answer += (i * 100) + j
        
  
  return answer


# print('Solution 1.', part_one())

print('Solution 2.', part_two())