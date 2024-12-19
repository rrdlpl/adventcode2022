from collections import deque


def parse_input():
  file = open('2024/day19/input.txt', 'r')
  lines = file.readlines()
  lines = [line.strip() for line in lines]
  
  towels = set([towel.strip() for towel in lines[0].split(',')])
  
  designs = []

  for i in range(2, len(lines)):
    design = lines[i].strip()
    designs.append(design)
  
  return towels, designs

def part_one():
  towels, designs = parse_input()

  def is_possible(design):
    queue = deque()
    queue.append(design)
    seen = set()

    while queue:
      d = queue.popleft()
      for towel in towels:
        if d.startswith(towel):
          new_s = d[len(towel):]
          # print(new_s)
          if not new_s:
            return True
          if new_s not in seen:
            seen.add(new_s)
            queue.append(new_s)
    return False

  result = 0
  for design in designs:
    if is_possible(design):
      result += 1
  
  return result


def part_two():
  towels, designs = parse_input()
  towels = list(towels)
  
  cache = {}

  def is_possible(design):
    def dfs(s):
      if not s:
        return 1
      if s in cache:
        return cache[s]
      count = 0
      for towel in towels:
        if s.startswith(towel):
          count += dfs(s[len(towel):])
      cache[s] = count
      return count
    return dfs(design)

  result = 0
  for design in designs:
    result += is_possible(design)
  
  return result

  

print('Solution 1.', part_one())
print('Solution 2.', part_two())

# attempts 400 too high