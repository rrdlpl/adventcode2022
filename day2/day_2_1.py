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

score = 0
for line in lines:
    game = line.split()
    enemy, me = game
    enemy = enemy.strip()
    me = me.strip()
    if myMap[me] == enemyMap[enemy]:
        score += 3
    elif (myMap[me] == 'paper' and enemyMap[enemy] == 'rock') or (myMap[me] == 'rock' and enemyMap[enemy] == 'scissors') or (myMap[me] == 'scissors' and enemyMap[enemy] == 'paper'):
        score += 6

    score += points[me]

print(score)
