
file = open('day25/input.txt', 'r')
lines = file.readlines()


def snafu_to_decimal(snafu):
    sum = 0
    map = {
        '=': -2,
        '-': -1
    }

    for i, digit in enumerate(snafu[::-1]):
        if digit in map:
            sum += (5 ** i) * map[digit]
        else:
            sum += (5 ** i) * int(digit)
    return sum


print('snafu', '2=-01', 'to dec = ', snafu_to_decimal('2=-01'), 976)

print(snafu_to_decimal('1=11-2'), 2022)


print(snafu_to_decimal('1121-1110-1=0'), 314159265)

print(snafu_to_decimal('1-0---0'), 12345)
