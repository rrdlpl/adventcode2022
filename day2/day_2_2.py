file = open('day2/input.txt', 'r')
lines = file.readlines()

myPoints = {
    'rock': 1,  # rock
    'paper': 2,  # paper
    'scissors': 3  # scissors
}

myAction = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win',
}

enemyMap = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors'
}

loseMap = {
    'rock': 'scissors',
    'scissors': 'paper',
    'paper': 'rock'
}

winMap = {
    'paper': 'scissors',
    'rock': 'paper',
    'scissors': 'rock'
}

# A  rock
# B  paper
# C  scissors
score = 0

for line in lines:
    # print('line', line)
    game = line.split()
    enemy, action = game
    enemy = enemy.strip()
    action = action.strip()

    if myAction[action] == 'draw':
        score += 3 + myPoints[enemyMap[enemy]]
    elif myAction[action] == 'lose':
       # print('enemy picked', enemyMap[enemy])
       # print('need to choose to lose', loseMap[enemyMap[enemy]])
        score += myPoints[loseMap[enemyMap[enemy]]]
    else:
       # print('enemy picked', enemyMap[enemy])
       # print('need to choose to win', winMap[enemyMap[enemy]])
        score += 6 + myPoints[winMap[enemyMap[enemy]]]


print(score)
