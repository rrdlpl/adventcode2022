
import re

file = open('2024/day3/input.txt', 'r')
lines = file.readlines()


def extract_and_multiply(data):
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


result = extract_and_multiply(''.join(lines))
    
  
print('Solution 2.', result)