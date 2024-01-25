import re




file = open('2023/day1/input.txt', 'r')
lines = file.readlines()

summe = 0

for line in lines:
  digits = re.findall(r'\d', line)
  n = digits[0] + digits[-1]
  summe += int(n)

print('Solution 1.', summe)