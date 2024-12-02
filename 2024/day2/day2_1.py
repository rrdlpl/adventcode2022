
file = open('2024/day2/input.txt', 'r')
lines = file.readlines()

result = 0
a = []
b = []

def is_safe(numbers):
  increasing = numbers[0] < numbers[1]
  for i in range(len(numbers) - 1):
    difference = numbers[i] - numbers[i + 1]
    if (increasing and difference > 0) or (not increasing and difference < 0):
      return False
    if abs(difference) < 1 or abs(difference) > 3:
      return False
  return True


for line in lines:
  numbers = line.split(' ') 
  a = [int(num) for num in numbers]
  safe = is_safe(a)
  if safe:
    result += 1
    continue
  
  for i in range(len(a)):
    b = a.copy()
    del b[i] 
    if is_safe(b):
      result +=1 
      break 
    
  
print('Solution 1.', result)