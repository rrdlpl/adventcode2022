
file = open('2024/day2/input.txt', 'r')
lines = file.readlines()

result = 0
a = []
b = []

def isSafe(a):
  is_increasing = a[0] < a[1]
  for i in range(len(a) - 1):
      # print('diff between ', a[i], 'and', a[i + 1], 'is', (a[i] - a[i + 1]))
      diff = a[i] - a[i + 1]
      if is_increasing and diff > 0:
        return False
      if not is_increasing and diff < 0:
        return False
      if abs(diff) < 1 or abs(diff) > 3:
        return False
  return True


for line in lines:
  numbers = line.split(' ') 
  a = [int(num) for num in numbers]
  safe = isSafe(a)
  if safe:
    result += 1
    continue
  
  for i in range(len(a)):
    b = a.copy()
    del b[i] 
    if isSafe(b):
      result +=1 
      break 
    
  
print('Solution 1.', result)