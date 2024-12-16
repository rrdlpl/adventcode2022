

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

def move_boxes_horizontally(map, current_position, dx):
  x, y = current_position
  possible_empty_box = (x, y + dx * 3)
  empty_box = None
  if 0 <= possible_empty_box[0] < len(map) and 0 <= possible_empty_box[1] < len(map[0]) and map[possible_empty_box[0]][possible_empty_box[1]] == '.':
    empty_box = possible_empty_box
  
  possible_empty_box = (x, y + dx * 5)
  if empty_box is None and 0 <= possible_empty_box[0] < len(map) and 0 <= possible_empty_box[1] < len(map[0]) and map[possible_empty_box[0]][possible_empty_box[1]] == '.': 
    empty_box = possible_empty_box
  
  if empty_box is None:
    return current_position
  
  if dx > 0:
    for j in range(empty_box[1], y - 1, -1):
      map[x][j] = map[x][j - 1]
    map[x][y] = '.'
    current_position = (x, y + dx)
    map[x][current_position[1]] = '@'
  else:
    for j in range(empty_box[1], y + 1):
      map[x][j] = map[x][j + 1]
    map[x][y] = '.'
    current_position = (x, y + dx)
    map[x][current_position[1]] = '@'
  
  return current_position

def move_boxes_vertically(map, current_position, dy):
  def can_move(box):
    return 0 <= box[0] < len(map) and 0 <= box[1] < len(map[0]) and map[box[0]][box[1]] == '.'
  x, y = current_position
  box = (x + dy, y)
  start_box_y, end_box_y = None, None
  if map[box[0]][box[1]] == '[':
    start_box_y = box[1]
    end_box_y = box[1] + 1
  else: 
    start_box_y =  box[1] - 1 
    end_box_y = box[1]
    
  possible_start_box, possible_end_box = (box[0] + dy, start_box_y), (box[0] + dy, end_box_y)
  empty_start_box = None
  empty_end_box = None
  if can_move(possible_start_box) and can_move(possible_end_box):
    empty_start_box = possible_start_box 
    empty_end_box = possible_end_box
    
  possible_start_box, possible_end_box = (box[0] + dy * 2, start_box_y), (box[0] + dy * 2, end_box_y)
  if can_move(possible_start_box) and can_move(possible_end_box) and empty_end_box is None and empty_start_box is None:
    empty_start_box = possible_start_box
    empty_end_box = possible_end_box
  
 
  if empty_end_box is None and empty_start_box is None:
    return current_position
  
  if dy < 0:
    # moving up
    for i in range(empty_start_box[0], x, 1):
      map[i][empty_start_box[1]] = map[i + 1][empty_start_box[1]]
    for i in range(empty_end_box[0], x, 1):
      map[i][empty_end_box[1]] = map[i + 1][empty_end_box[1]]
    map[current_position[0]][y] = '.'
    current_position = (current_position[0] + dy, current_position[1])
    map[current_position[0]][current_position[1]] = '@'
  else:
    # moving down
    for i in range(empty_start_box[0], x, -1):
      map[i][empty_start_box[1]] = map[i - 1][empty_start_box[1]]
    for i in range(empty_end_box[0], x, -1):
      map[i][empty_end_box[1]] = map[i - 1][empty_end_box[1]]
    map[current_position[0]][y] = '.'
    current_position = (current_position[0] + dy, current_position[1])
    map[current_position[0]][current_position[1]] = '@'
  
  return current_position
 

  
  
def part_two():
  
  grid, instructions = parse_input()
  map = resize_map(grid)
  current_position = init_2(map)
  render_grid(map)

  for instruction in instructions:
    dx, dy = move(instruction)
    print("Move: ", instruction, "\n")
    next_position = (current_position[0] + dy, current_position[1] + dx)
    
    if map[next_position[0]][next_position[1]] == '#':
      render_grid(map)
      continue
    if map[next_position[0]][next_position[1]] == '.':
      map[current_position[0]][current_position[1]] = '.'
      map[next_position[0]][next_position[1]] = '@'
      current_position = next_position
      render_grid(map)
      continue
    if instruction == '>' or instruction == '<':
      current_position = move_boxes_horizontally(map, current_position, dx)
      render_grid(map)
      continue
    if instruction == 'v' or instruction == '^':
      current_position = move_boxes_vertically(map, current_position, dy)
      render_grid(map)
      continue

        

    
  
  return 0


# print('Solution 1.', part_one())

print('Solution 2.', part_two())