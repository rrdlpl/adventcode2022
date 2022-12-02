file = open('day2/input.txt', 'r')
lines = file.readlines()

points = {
    'rock': 1,  # rock
    'paper': 2,  # paper
    'scissors': 3  # scissors
}

actions = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win',
}

enemyMap = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors'
}

lose = {
    'rock': 'scissors',
    'scissors': 'paper',
    'paper': 'rock'
}

win = {
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

    if actions[action] == 'draw':
        score += 3 + points[enemyMap[enemy]]
    elif actions[action] == 'lose':
       # print('enemy picked', enemyMap[enemy])
       # print('need to choose to lose', loseMap[enemyMap[enemy]])
        score += points[lose[enemyMap[enemy]]]
    else:
       # print('enemy picked', enemyMap[enemy])
       # print('need to choose to win', winMap[enemyMap[enemy]])
        score += 6 + points[win[enemyMap[enemy]]]


print(score)
