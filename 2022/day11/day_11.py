import time
new = 0
test = ' old * 19'
# test.replace('old', str(4))
print('testing', test)

print(type(test))
old = 2
new = eval(test)
print(new)
print('new', new)


class Monkey:
    def __init__(self, group) -> None:
        self.inspect_count = 0
        self.name = group[0]
        self.items = [int(s) for s in group[1].replace(
            'Starting items: ', '').split(',')]
        self.expression = group[2].replace('Operation: new =', '')
        self.divisor = int(group[3].replace('Test: divisible by ', ''))
        self.true = int(group[4].replace('If true: throw to monkey ', ''))
        self.false = int(group[5].replace('If false: throw to monkey ', ''))

    def inspect(self, modulo):
        next_monkeys = [[], []]
        n = len(self.items)

        for i in range(n):
            old = self.items[i]
            # print(self.name, ' inspects item ', old)

            new = eval(self.expression)  # // 3
            new = new % modulo

            # print('New item worry level', new)
            if new % self.divisor == 0:
                # print('New item is divisible by ', self.divisor,
                #   ' it goes to monkey ', self.true)
                next_monkeys[0].append(new)
            else:
                # print('New item is NOT divisible by ', self.divisor,
                #   ' it goes to monkey ', self.false)
                next_monkeys[1].append(new)
            self.inspect_count += 1
        self.items = []
        return next_monkeys

    def catch(self, items):
        for item in items:
            self.items.append(item)

    def print_monkey(self):
        print(self.name)
        print('Items: ', self.items)
        print('Operation: ', self.expression)
        print('Divisor = ', self.divisor)
        print('Throw if true', self.true)
        print('Throw if false', self.false)


def create_monkeys(lines):
    monkeys = []
    line_groups = []
    while len(lines) > 0:
        line_group = []
        for i in range(6):
            line_group.append(lines[i].strip())
        lines = lines[7:]

        line_groups.append(line_group)

    for group in line_groups:
        monkey = Monkey(group)
        monkeys.append(monkey)
    return monkeys


def start_inspecting(monkeys):

    modulo = 1
    for monkey in monkeys:
        modulo *= monkey.divisor
    print('Modulo', modulo)

    for i in range(10000):

        for actual_monkey in monkeys:
            throw_items = actual_monkey.inspect(modulo)
            monkeys[actual_monkey.true].catch(throw_items[0])
            monkeys[actual_monkey.false].catch(throw_items[1])
        # print('')
        if (i + 1) in [1, 20, 25]:
            print()
            print('Round i', i + 1)
            print()
            for i in range(len(monkeys)):
                print(monkeys[i].name, monkeys[i].items)

            for i in range(len(monkeys)):
                print(monkeys[i].name, 'inspect count ',
                      monkeys[i].inspect_count)

    print('\n Inspect count \n')
    inspect = []
    for i in range(len(monkeys)):
        inspect.append(monkeys[i].inspect_count)
        print(monkeys[i].name, monkeys[i].inspect_count)

    inspect = sorted(inspect, reverse=True)
    print(inspect)
    print('Solution 2', inspect[0] * inspect[1])


file = open('day11/input.txt', 'r')
lines = file.readlines()


monkeys = create_monkeys(lines)
start_inspecting(monkeys)

start_time = time.time()

end_time = time.time()
print('Time ellapsed', (end_time - start_time) * 1000)

file.close()
