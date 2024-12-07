import time


file = open('2024/day7/input.txt', 'r')
lines = file.readlines()




def part_one():
  def dfs(target, candidates, total, i):
    if i == len(candidates):
      return total == target
    
    if total + candidates[i] <= target and dfs(target, candidates, total + candidates[i], i + 1):
      return True
    if total * candidates[i] <= target and dfs(target, candidates, total * candidates[i], i + 1):
      return True

    
    return False
  
  result = 0
  for line in lines:
    line = line.strip()
    line = line.split()
    target = int(line[0].replace(':', ''))
    
    candidates = [int(num)  for num in line[1:]]
    
    if dfs(target, candidates, 0, 0):
      result += target
    
  return result


def part_two():
  
  def dfs(target, candidates, total, i):
    if i == len(candidates):
      return total == target
    
    if total + candidates[i] <= target and dfs(target, candidates, total + candidates[i], i + 1):
      return True
    if total * candidates[i] <= target and dfs(target, candidates, total * candidates[i], i + 1):
      return True
    concat = int(str(total) + str(candidates[i]))
    if concat <= target and dfs(target, candidates, concat, i + 1):
      return True
    
    return False
  
  result = 0
  for line in lines:
    line = line.strip()
    line = line.split()
    target = int(line[0].replace(':', ''))
    candidates = [int(num)  for num in line[1:]]
    if dfs(target, candidates, 0, 0):
      result += target
    
  return result

time_start = time.time()
result_one = part_one()
time_end = time.time()
print('Solution 1. ', result_one)
print('Time ellapsed: ', (time_end - time_start) * 1000, 'ms')

time_start = time.time()
result_two = part_two()
time_end = time.time()
print('Solution 2. ', result_two)
print('Time ellapsed: ', (time_end - time_start) * 1000, 'ms')