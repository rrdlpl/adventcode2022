sum = 0
sum += 3 + 2 + 2 + 0 + 0  # rock 30 heighest 51
sum += 2 + 3 + 4 + 0 + 1  # rock 35 heighest 61
sum += 2 + 1 + 2 + 0 + 1  # rock 40 heighest 67
sum += 2 + 1 + 2 + 0 + 1  # rock 45 heighest 73
sum += 3 + 2 + 0 + 0 + 1  # rock 50 heighest 79
sum += 3 + 3 + 4 + 0 + 1  # rock 55 heighest 90
sum += 2 + 3 + 0 + 1 + 1  # rock 60 heighest 97

print('Sum', sum)


n = (100_000_000_0000 - 20) / 35


print('n', n)
print('Solution 2', (n * sum) + 36)
