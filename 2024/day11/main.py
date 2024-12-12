import time
file = open('2024/day11/input.txt', 'r')
lines = ''.join(file.readlines())



def part_one(blinking_times):
  stones = lines.split()

  for _ in range(int(blinking_times)):
    new_stones = []

    for j in range(len(stones)):
      if stones[j] == '0':
        new_stones.append('1')
      elif len(stones[j]) % 2 == 0:
        stone_str = str(stones[j])
        mid = len(stone_str) // 2
        first_half = int(stone_str[:mid])
        second_half = int(stone_str[mid:])
        new_stones.append(str(int(first_half)))
        new_stones.append(str(int(second_half)))
      else:
        new_stones.append(str(int(stones[j]) * 2024))

    stones = new_stones.copy()
    # print(' '.join(stones))
  return len(stones)              
  

def part_two(blinking_times):
  cache = {}
  def blink(stone, blinking_times):
    if (stone, blinking_times) in cache:
      return cache[(stone, blinking_times)]
    if blinking_times == 0:
      return 1
    result = 0 
    stone_str = str(stone)
    if stone == 0:
      result = blink(1, blinking_times - 1)
    elif (len(stone_str) % 2 == 0):
      mid = len(stone_str) // 2
      first_half = int(stone_str[:mid])
      second_half = int(stone_str[mid:])
      result += blink(first_half, blinking_times - 1) + blink(second_half, blinking_times - 1)
    else:
      result += blink(stone * 2024, blinking_times - 1)
    # print('cache', cache)  
    cache[(stone, blinking_times)] = result
    return result
  
  # print(' '.join(stones))
  answer = 0
  for stone in lines.split():
    answer += blink(int(stone), blinking_times)
  return answer

print('Solution 1.', part_one(25))
print('Solution 2.', part_two(75))
# 29165
# 62
# 9387