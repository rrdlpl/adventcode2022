

file = open('day3/input.txt', 'r')
lines = file.readlines()


# {'J': 2, 'r': 2, 'w': 2, 'W': 2, 'v': 1, 'p': 1, 't': 1, 'g': 1}
result = 0
for line in lines:
    a = set(list(line[:len(line)//2]))
    b = set(list(line[len(line)//2:]))
    intersect = a.intersection(b)
    for character in intersect:
        if character.islower():
            order = ord(character) - 96
            result += order
            print('Order lowercased', character, order)
        else:
            order = ord(character) - 64 + 26
            result += order
            print('Order capital', character, order)

print(result)
