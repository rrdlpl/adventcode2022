import re

file = open('2023/day1/input.txt', 'r')
lines = file.readlines()

summe = 0
numbers = "one two three four five six seven eight nine".split()
pattern = "(?=(" + "|".join(numbers) + "|\\d))"

print('fdf', pattern)


def f(x):
    if x in numbers:
        return str(numbers.index(x) + 1)
    return x


for line in lines:
    digits = [*map(f, re.findall(pattern, line))]
    summe += int(digits[0] + digits[-1])

print('Solution 2.', summe)