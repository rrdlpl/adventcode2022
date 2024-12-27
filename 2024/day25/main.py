def parse_inputs():
  grids = open('2024/day25/input.txt', 'r').read().strip().split('\n\n')
  
  locks = []
  keys = []

  for grid in grids:
    if grid.startswith('#'):
      locks.append(get_height(grid))
    else:
      keys.append(get_height(grid))

  
  return locks, keys


def get_height(grid):
  g = [list(line.strip()) for line in grid.split('\n')]
  heights = [-1] * len(g[0])
  for j in range(len(g[0])):
    for i in range(len(g)):
      if g[i][j] == '#':
        heights[j] += 1
      
  return heights


def part_one():
  locks, keys = parse_inputs()
  print('Locks', locks)
  print('keys', keys)
  
  result = 0

  def fit(lock, key):
    for i in range(len(lock)):
      if lock[i] + key[i] > 5:
        return False
    return True
  
  for lock in locks:
    for key in keys:
      if fit(lock, key):
        result += 1
  return result


print('Solution 1', part_one())