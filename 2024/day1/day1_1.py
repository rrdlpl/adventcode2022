import re




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
b.sort()

for i in range(len(a)):
  result  += abs(a[i] - b[i])

print('Solution 1.', result)