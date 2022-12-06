file = open('day6/input.txt', 'r')
line = file.readlines()[0]


def start_of(line, size) -> int:
    for i in range(0, len(line) - size):
        s = set(line[i:(i + size)])
        if len(s) == size:
            return i + size
    return -1


print('solution 1', start_of(line, 4))
print('solution 2', start_of(line, 14))
file.close()
