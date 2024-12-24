class OperatorParser:
  def __init__(self, operation):
    self.operation = operation
    op = operation.split('->')
    left, key = op
    self.key = key.strip()
    left = left.split(' ')
    self.left_key = left[0]
    self.right_key = left[2]
    self.operator = left[1]
  
  
    
def parse_input():
  wire_file = open('2024/day24/input.txt', 'r')
  lines = wire_file.readlines()
  wires = {}
  

  for i in range(0, len(lines)):
    line = lines[i].strip()
    if line == '':
      break;
    left, right = line.split(':')
    left = left.strip()
    right = right.strip()
    wires[left] = int(right)
  
  operations = []
  for j in range(i + 1, len(lines)):
    line = lines[j].strip()
    operations.append(line)
  # print(operations)
  return wires, operations


def evaluate(map, key):
    if isinstance(map[key], int):
        return map[key]

    parser = map[key]
    left, right = parser.left_key, parser.right_key
    if parser.operator == 'AND':
        result = evaluate(map, left) & evaluate(map, right)
    elif parser.operator == 'OR':
        result = evaluate(map, left) | evaluate(map, right)
    elif parser.operator == 'XOR':
        result = evaluate(map, left) ^ evaluate(map, right)
    map[parser.key] = result
    return result
  
def binary_to_decimal(binary_str):
    return int(binary_str, 2)
def part_one():
  wires, operations = parse_input()
  to_solve_keys = []
  for operation in operations:
    parser = OperatorParser(operation)
    wires[parser.key] = parser
    if parser.key.startswith('z'):
      to_solve_keys.append(parser.key)
  result = []  
  to_solve_keys.sort(reverse=True)
  
  for key in to_solve_keys:
    result.append(evaluate(wires, key))

  return binary_to_decimal(''.join([str(r) for r in result]))

  


print('Solution 1.', part_one())