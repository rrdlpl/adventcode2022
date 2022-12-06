

from collections import Counter


file = open('day6/input.txt', 'r')
line = file.readlines()[0]
size = 14  # 4

for i in range(1, len(line)):
    s = Counter(line[i:(i+size)])
    if len(s) == size:
        result = i + size
        break

print(result)
file.close()
