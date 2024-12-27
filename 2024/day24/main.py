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
  
  
  for j in range(i + 1, len(lines)):
    line = lines[j].strip()
    operation = OperatorParser(line)
    wires[operation.key] = operation
  # print(operations)
  return wires


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

def get_in_known_terms(map, key):
   if key.startswith('x') or key.startswith('y'):
        return key
   if isinstance(map[key], str):
    return  map[key]
      
   parser = map[key]
   
   left, right = parser.left_key, parser.right_key
   if (left.startswith('x') or left.startswith('y')) and (right.startswith('x') or right.startswith('y')):
     if left[1:] != right[1:]:
        print('alert', key,  left[1:], right[1:])

   
   if parser.operator == 'AND':
        result = '(' + get_in_known_terms(map, left) + ' AND ' + get_in_known_terms(map, right) + ')'
   elif parser.operator == 'OR':
        result = '(' + get_in_known_terms(map, left) + ' OR ' + get_in_known_terms(map, right) + ')'
   elif parser.operator == 'XOR':
        result = '(' + get_in_known_terms(map, left) + ' XOR ' + get_in_known_terms(map, right) + ')'
   map[parser.key] = result
   return result
  
def find_swaps(wires, operations):
  to_solve_keys = []
  for operation in operations:
    parser = OperatorParser(operation)
    wires[parser.key] = parser
    if parser.key.startswith('z')  :
        to_solve_keys.append(parser.key) 
    if parser.key.startswith('z') and parser.operator != 'XOR':
      print('Wrong gate', parser.key, parser.operation)
  
  to_solve_keys.sort()
  
  swapps = []
  in_correct_order = []
  
  for key in wires.keys():
    s = get_in_known_terms(wires, key)
    swapps.append(key+'= '+s)
  swapps.sort(key=lambda x: len(x))
  
  # for s in swapps:
  #   print(s)
  return swapps


  
def solve(wires):
  to_solve_keys = []
  for key in wires.keys():
    # parser = OperatorParser(operation)
    # wires[parser.key] = parser
    if key.startswith('z'):
     to_solve_keys.append(key)
  result = []  
  to_solve_keys.sort(reverse=True)
  
  for key in to_solve_keys:
    result.append(evaluate(wires, key))

  return ''.join([str(r) for r in result])
                           
def part_two():
  wires = parse_input()
  x = []
  y = []
  s = []
  
  # ff = find_swaps(wires, operations)
  for key in wires.keys():
    if key.startswith('x'):
      x.append(key)
    elif key.startswith('y'):
      y.append(key)
    else:
      s.append(key)
  
  x.sort(reverse=True)
  y.sort(reverse=True)
  
  actual_x = binary_to_decimal(''.join([str(wires[k]) for k in x]))
  actual_y = binary_to_decimal(''.join([str(wires[k]) for k in y]))
  
  actual_value = actual_x + actual_y
  
  print('X + Y = ', actual_value)
  
  swaps = [("qnw", "z15"), ('z20', 'cqr'), ('z37', 'vkg'), ('ncd', 'nfj')]
  for a,b in swaps:
    wires[a], wires[b] = wires[b], wires[a]
  
  print('    Z = ', binary_to_decimal(solve(wires)))
  


# attempts
# msn,ncd,qnw,trt,vkg,z15,z20,z37
# msn,ncd,nfj,qnw,vkg,z15,z20,z37
# mmj,msn,ncd,qnw,vkg,z15,z20,z37
# cqr,mmj,ncd,qnw,vkg,z15,z20,z37
# cqr,ncd,nfj,qnw,vkg,z15,z20,z37
# cqr,ncd,nfj,qnw,vkg,z15,z20,z37
      
  # def swap(wires, a, b , c,)
  # for i in range(0, len(s)):
  #   for j in range(i + 1, len(s)):
  #     for k in range(j + 1, len(s)):
  #       for l in range(k + 1, len(s)):
  #         w = wires.copy()
          
          
  
# def part_two():
#   wires, operations = parse_input()
#   x = []
#   y = []
#   swappables = []
#   for key in wires.keys():
#     if key.startswith('x'):
#       x.append(key)
#     elif key.startswith('y'):
#       y.append(key)
#     else:
#       swappables.append(key)
    
#   x.sort(reverse=True)
#   actual_x = binary_to_decimal(''.join([str(wires[k]) for k in x]))
#   actual_y = binary_to_decimal(''.join([str(wires[k]) for k in y]))
#   actual_value = actual_x * actual_y
#   print('Actual Value = ', actual_value)
#   actual = (bin(actual_value)).split("b")[-1]
#   print('Actual binary = ', actual)
  
 
  
#   swapps = find_swaps(wires, operations)
  
#   for swapp in swapps: 
    
  
  
  
  


# print('Solution 1.', part_one())

print('Solution 2.', part_two())

# attempt