
file = open('2024/day3/input.txt', 'r')
lines = file.readlines()

result = 0

import re

def extract_and_multiply(data):
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    
    matches = re.findall(pattern, data)
    
    results = 0
    for match in matches:
        numbers = re.findall(r'\d+', match)
        x, y = map(int, numbers)
        
        results += x * y
    
    return results

for line in lines:
    result += extract_and_multiply(line)
    
  
print('Solution 1.', result)