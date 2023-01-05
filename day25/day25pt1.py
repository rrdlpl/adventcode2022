
file = open('day25/input.txt', 'r')
lines = file.readlines()


def snafu_to_decimal(snafu):
    decimal = 0
    map = {
        '=': -2,
        '-': -1
    }
    for i, digit in enumerate(snafu[::-1]):
        if digit in map:
            decimal += (5 ** i) * map[digit]
        else:
            decimal += (5 ** i) * int(digit)
    return decimal


def decimal_to_snafu(decimal):
    map = {
        0: "0",
        1: "1",
        2: "2",
        -2: "=",
        -1: "-",
    }
    snafu = ''
    while decimal > 0:
        mod = ((decimal + 2) % 5) - 2
        snafu = map[mod] + snafu
        decimal = ((decimal + 2)) // 5
    return snafu


print('snafu', '2=-01', 'to dec = ', snafu_to_decimal('2=-01'), 976)

print(snafu_to_decimal('1=11-2'), 2022)


print(snafu_to_decimal('1121-1110-1=0'), 314159265)

print(snafu_to_decimal('1-0---0'), 12345)


def part_one(lines):
    sum = 0
    for line in lines:
        line = line.strip()
        sum += snafu_to_decimal(line)
    return sum


sol = part_one(lines)

print('Solution 1 decimal', sol)
print('Solution 1 snafu', decimal_to_snafu(sol))

print(snafu_to_decimal('2=-1=0'), 4890)


# print('Snafu to decimal ', snafu_to_decimal('124030'))
# '2=-1=0'
# '124030'
