file = open('day2/input.txt', 'r')
lines = file.readlines()

points = {
    'Y': 2,  # paper
    'X': 1,  # rock
    'Z': 3  # scissors
}

myMap = {
    'X': 'rock',
    'Y': 'paper',

    'Z': 'scissors'
}

enemyMap = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors'
}

# A  rock
# B  paper
# C  scissors
score = 0
w = 0
l = 0
t = 0
for line in lines:
    print('line', line)
    game = line.split()
    enemy, me = game
    enemy = enemy.strip()
    me = me.strip()
    print('me', myMap[me], enemyMap[enemy])
    if myMap[me] == enemyMap[enemy]:
        score += 3 + points[me]
    elif (myMap[me] == 'paper' and enemyMap[enemy] == 'rock') or (myMap[me] == 'rock' and enemyMap[enemy] == 'scissors') or (myMap[me] == 'scissors' and enemyMap[enemy] == 'paper'):
        score += 6 + points[me]
    else:
        score += points[me]

print(w, l, t)
print(score)
