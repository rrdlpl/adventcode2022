import time


file = open('2024/day6/input.txt', 'r')
lines = file.readlines()

start_point = None
obstacles = set()
visited_in_part_one = set()
for i, line in enumerate(lines):
  for j, char in enumerate(line.strip()):
    if char == '.':
      continue
    if char == '#':
      obstacles.add((i, j))
    if char == '^':
      start_point = (i, j)


def part_one():
  visited = set()
  def dfs(x, y):
    if x < 0 or x >= len(lines) or y < 0 or y >= len(lines[0]):
      return
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    current_direction = 0
    while 0 <= x < len(lines) and 0 <= y < len(lines[0]):
      visited.add((x, y))
      visited_in_part_one.add((x, y))
      dx, dy = directions[current_direction]
      new_x, new_y = x + dy, y + dx
      if (new_x, new_y) in obstacles:
        current_direction = (current_direction + 1) % len(directions)
        continue
      x, y = new_x, new_y
    return len(visited)
  
  return dfs(start_point[0], start_point[1])


def part_two():
  total_cycles = 0
  for x, y in visited_in_part_one: 
      if (x, y) in obstacles:
        continue
      obstacles.add((x, y))
      visited = set()
      def dfs(x, y):
        if x < 0 or x >= len(lines) or y < 0 or y >= len(lines[0]):
          return
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        current_direction = 0
        while 0 <= x < len(lines) and 0 <= y < len(lines[0]):
          dx, dy = directions[current_direction]
          new_x, new_y = x + dy, y + dx
          if (new_x, new_y) in obstacles:
            current_direction = (current_direction + 1) % len(directions)
            continue
          if (new_x, new_y, current_direction) in visited:
            return True
          x, y = new_x, new_y
          visited.add((x, y, current_direction))
        return False
      
      visited.add((start_point[0], start_point[1], 0))
      if dfs(start_point[0], start_point[1]):
        total_cycles += 1
      obstacles.remove((x, y))
  return total_cycles
  
  


print('Solution 1', part_one())

start = time.time()
solution_2 = part_two()
end = time.time()
print('Solution 2', solution_2, end - start, 'sec')