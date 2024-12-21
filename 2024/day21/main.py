
from collections import defaultdict, deque
from functools import cache


def parse_input():
  file = open('2024/day21/input.txt', 'r')
  
  return [line.strip() for line in file.readlines()]


numeric_keypad = [
  ['7', '8', '9'],
  ['4', '5', '6'],
  ['1', '2', '3'],
  ['#', '0', 'A']
]

direction_keypad = [
  ['#', '^', 'A'],
  ['<', 'v', '>'],
]

reverse_direction_keypad = {
  (0, 1): '>',
  (0, -1): '<',
  (1, 0): 'v',
  (-1, 0): '^',
}



def find_key_position(keypad, key):
  for i in range(len(keypad)):
    for j in range(len(keypad[i])):
      if key == keypad[i][j]:
        return (i, j)
      
def find_all_paths(keypad, start_key, end_key):
  def can_move(row, col, keypad):
    return 0 <= row < len(keypad) and 0 <= col < len(keypad[0]) and keypad[row][col] != '#'
  
  start = find_key_position(keypad, start_key)
  end = find_key_position(keypad, end_key)
  queue = deque()
  queue.append((start, 0, '^', []))
  
  all_paths = []
  min_steps =  float('inf')
  while queue:
    current_position, steps, _, path = queue.popleft()
    if steps > min_steps:
      continue
    if current_position == end:
      if steps <= min_steps:
        all_paths.append(''.join(p[2] for p in path) + 'A')
        min_steps = steps
      continue
    row, col = current_position 
    for dr, dc in reverse_direction_keypad.keys():
      new_row, new_col = row + dr, col + dc
      if can_move(new_row, new_col, keypad):
        new_path = path.copy()
        new_direction = reverse_direction_keypad[(dr, dc)]
        new_path.append((new_row, new_col, new_direction))
        queue.append(((new_row, new_col), steps + 1, new_direction, new_path))
  
  return all_paths

@cache
def min_length_direction_keypads(sequence: str, robots: int) -> int:
    if robots == 0:
        return len(sequence)
    total = 0
    previous = "A"
    for current in sequence:
        all_sequences = find_all_paths(direction_keypad, previous, current)
        all_subsequences_lengths = [min_length_direction_keypads(sequence, robots - 1) for sequence in all_sequences]
        total += min(all_subsequences_lengths)
        previous = current
    return total
  
def find_complexity(code: str, robots: int) -> int:
    previous = "A"
    total = 0
    for key in code:
        all_paths = find_all_paths(numeric_keypad, previous, key)
        a = [min_length_direction_keypads(sub_sequence, robots) for sub_sequence in all_paths]
        previous = key
        total += min(a)
    return total * int(code.replace('A', ''))
def find_total_complexity(codes, robots):
    return sum(find_complexity(code, robots) for code in codes)
def combine_paths(paths1, paths2):
  new_paths = []
  for path1 in paths1:
    for path2 in paths2:
      new_paths.append(path1 + path2)
  return new_paths
def part_one():
  codes = ['413A', '480A', '682A', '879A', '083A']
  return find_total_complexity(codes, 2)

def part_two():
  codes = ['413A', '480A', '682A', '879A', '083A']
  return find_total_complexity(codes, 25)
  # for code in codes:

  #   stack = find_all_paths(numeric_keypad, 'A', code[0])
  #   for i in range(1, len(code)):
  #     new_paths = combine_paths(stack, find_all_paths(numeric_keypad, code[i - 1], code[i]))
  #     stack = new_paths
    
  # print('All paths numeric ath', stack)
  
  # for path in stack:
  #   direction_stack = find_all_paths(direction_keypad, 'A', path[0])
  #   for i in range(1, len(path)):
  #     new_paths = combine_paths(direction_stack, find_all_paths(direction_keypad, path[i - 1], path[i]))
  #     direction_stack = new_paths
      
  
    
      
  # for direction in set(direction_stack):
  #     print(direction)
  # return direction_stack


print('Solution 1.', part_one())
print('Solution 2. ', part_two())

# print('Solution 1.', )
# print(find_all_paths(numeric_keypad, 'A', '0'))
# print(find_all_paths(numeric_keypad, '0', '2'))
# print(find_all_paths(numeric_keypad, '2', '9'))
# print(find_all_paths(numeric_keypad, '9', 'A'))


# print(find_all_paths(direction_keypad, 'A', '<'))
# print(find_all_paths(direction_keypad, '<', 'A'))
# print(find_all_paths(direction_keypad, 'A', '^'))
# print(find_all_paths(direction_keypad, '^', 'A'))