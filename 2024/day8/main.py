
from collections import defaultdict


file = open('2024/day8/input.txt', 'r')
lines = file.readlines()

grid = [list(line.strip()) for line in lines]
m = len(grid)
n = len(grid[0])

antennas = defaultdict(lambda: [])

def print_grid():
  for i in range(m):
    print(''.join(grid[i]))

def add_antinode(antinodes, a, b):
   dx, dy = a[0] - b[0], a[1] - b[1]
   nx, ny = b[0] - dx,  b[1] - dy
   if 0 <= nx < m and 0 <= ny < n:
     antinodes.add((nx,ny))
    

def add_antinode2(antinodes, a, b):
   dx, dy = a[0] - b[0], a[1] - b[1]
   nx, ny = b[0] ,  b[1] 
   while 0 <= nx < m and 0 <= ny < n:
     antinodes.add((nx,ny))
     nx, ny = nx - dx, ny - dy

def part_one():
  for i in range(m):
    for j in range(n):
      if grid[i][j] == '.':
        continue
      antenna = grid[i][j]
      antennas[antenna].append((i, j))
  antinodes = set()
  for key in antennas.keys():  
     for i in range(len(antennas[key])):
        for j in range(len(antennas[key])):
            if i == j:
              continue
            add_antinode(antinodes, antennas[key][i],  antennas[key][j])

  print_grid()
  print('antinodes')
  print(antinodes)
  return len(antinodes)

def part_two():
  antinodes = set()
  for key in antennas.keys():  
     for i in range(len(antennas[key])):
        for j in range(len(antennas[key])):
            if i == j:
              continue
            add_antinode2(antinodes, antennas[key][i],  antennas[key][j])
  return len(antinodes)


print('Solution 1.',  part_one())
print('Solution 2.',  part_two())