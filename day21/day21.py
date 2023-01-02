

file = open('day21/input.txt', 'r')
lines = file.readlines()

map = {}

for line in lines:
    line = line.strip()
    left, right = line.split(':')
    left = left.strip()
    right = right.strip()

    if '+' in right or '-' in right or '*' in right or '/' in right.strip():
        map[left] = right.strip()
    else:
        map[left] = float(right.strip())


def evaluate(map, key):
    if isinstance(map[key], float):
        return map[key]

    result = 0
    if '+' in map[key]:
        left, right = map[key].split('+')
        result = evaluate(map, left.strip()) + evaluate(map, right.strip())
    elif '-' in map[key]:
        left, right = map[key].split('-')
        result = evaluate(map, left.strip()) - evaluate(map, right.strip())
    elif '*' in map[key]:
        left, right = map[key].split('*')
        result = evaluate(map, left.strip()) * evaluate(map, right.strip())
    elif '/' in map[key]:
        left, right = map[key].split('/')
        result = evaluate(map, left.strip()) / evaluate(map, right.strip())

    return result


print('root = ', evaluate(map, 'root'))
print('sbtm = ', evaluate(map, 'sbtm'))
print('bmgf = ', evaluate(map, 'bmgf'))

map['humn'] = 1.0

low = 0
high = 3000_000_000_000_000

while True:
    map['humn'] = (low + high) / 2
    a = evaluate(map, 'sbtm')
    b = evaluate(map, 'bmgf')

    if a == b:
        print('Solution 2', map['humn'])
        break

    if a < b:

        high = map['humn']
    else:
        low = map['humn']

    print('dfsdf', map['humn'])

print('root = ', evaluate(map, 'root'))

sbtm = evaluate(map, 'sbtm')
bmgf = evaluate(map, 'bmgf')

if sbtm > bmgf:
    print('more')
else:
    print('less')
print('sbtm = ', sbtm)
print('bmgf = ', bmgf)
