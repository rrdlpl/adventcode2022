

file = open('day3/input.txt', 'r')
lines = file.readlines()


result = 0
count = 0
a = set()
for line in lines:
    if count % 3 == 0:
        a = set(list(line.strip()))
    else:
        a = a.intersection(set(list(line.strip())))

    count += 1
    if count % 3 == 0:
        for character in a:
            if character.islower():
                order = ord(character) - 96
                result += order
                print('Order lowercased', character, order)
            else:
                order = ord(character) - 64 + 26
                result += order
                print('Order capital', character, order)
print(result)
