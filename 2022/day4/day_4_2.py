

file = open('day4/input.txt', 'r')
lines = file.readlines()


result = 0

for line in lines:

    line = line.strip()
    left, right = line.split(',')
    minA, maxB = left.split('-')
    # print(minA, maxB)
    a = set(range(int(minA), int(maxB) + 1))

    minA, maxB = right.split('-')
    # print(minA, maxB)
    b = set(range(int(minA), int(maxB) + 1))

    if a.intersection(b) or b.intersection(a):
        result += 1

print(result)
