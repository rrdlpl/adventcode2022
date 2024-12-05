
import re
file = open('2024/day3/input.txt', 'r')
lines = file.readlines()

def part_one(data):
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    
    matches = re.findall(pattern, data)
    
    results = 0
    for match in matches:
        numbers = re.findall(r'\d+', match)
        x, y = map(int, numbers)
        
        results += x * y
    
    return results

def part_two(data):
    result = 0
    enabled_multiplication = True
    for match in re.findall(r'don\'t\(\)|do\(\)|mul\(\d+,\d+\)', data):
        match match:
            case 'do()':
                enabled_multiplication = True
            case 'don\'t()':
                enabled_multiplication = False
            case _:
                if enabled_multiplication:
                    numbers = re.findall(r'\d+', match)
                    x, y = map(int, numbers)
                    result += x * y

    return result

    
print('Solution 1.', part_one(''.join(lines)))

print('Solution 2.', part_two(''.join(lines)))