from typing import Counter




file = open('2024/day1/input.txt', 'r')
lines = file.readlines()

result = 0
a = []
b = []
for line in lines:
  numbers = line.split(' ') 
  a.append(int(numbers[0]))
  b.append(int(numbers[-1]))


a.sort()
b = Counter(b)

for i in range(len(a)):
  result  += a[i] * b[a[i]] 

print('Solution 1.', result)