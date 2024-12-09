import time


file = open('2024/day9/input.txt', 'r')
lines = file.readlines()

def parse_input(lines):
  line = ''.join(line.strip() for line in lines)
  disk_map = []
  file_id = 0
  files = []
  free_blocks = []
  for file in range(0, len(line), 2):
    file_start = len(disk_map)
    for _ in range(int(line[file])):
      disk_map.append(file_id)
    file_end = len(disk_map) - 1
    files.append((file_id, int(line[file]), file_start, file_end))
    
    if file + 1 >= len(line):
      break
    free_block_start = len(disk_map) 
    for _ in range(int(line[file + 1])):
      disk_map.append('.')
    
    free_block_end = len(disk_map) - 1
    free_blocks.append((file_id, int(line[file + 1]), free_block_start, free_block_end))
    file_id += 1

  return disk_map, files, free_blocks
def part_one():
  disk_map, _ , _ = parse_input(lines)
  left = 0 
  right = len(disk_map) - 1
  while left < right:
    while disk_map[left] != '.':
      left += 1
    while disk_map[right] == '.':
      right -= 1
    if left >= right:
      break 
    disk_map[left], disk_map[right] = disk_map[right], disk_map[left]
    

  return checksum(disk_map)

def checksum(disk_map):
    return sum(idx * file_id for idx, file_id in enumerate(disk_map) if file_id != '.')


def part_two():
  disk_map, files, free_blocks = parse_input(lines)

  for file_id, file_size, file_start, file_end in reversed(files):
    for i in range(len(free_blocks)):
      free_id, free_size, fb_start, fb_end = free_blocks[i]
      if free_size >= file_size and fb_start < file_start:
        for k in range(file_start, file_start + file_size):
          disk_map[k] = '.'
        for j in range(fb_start, fb_start + file_size):
          disk_map[j] = file_id
        free_blocks[i] = (free_id, free_size - file_size, fb_start + file_size, fb_end)
        
        break
  return checksum(disk_map)


print('Solution 1.', part_one())
print('Solution 2.', part_two())