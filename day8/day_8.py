file = open('day8/input.txt', 'r')
lines = file.readlines()


def build_matrix(lines):
    matrix = []
    for line in lines:
        line = line.strip()
        row = [int(s) for s in list(line)]
        matrix.append(row)

    return matrix


def count_visible_trees(matrix):
    m = len(matrix)
    n = len(matrix[0])
    print('M x N', m, n)
    visited = set()
    count = 0
    for i in range(1, m - 1):
        max_visible_height_top = matrix[0][i]
        max_visible_height_left = matrix[i][0]
        max_visible_height_bottom = matrix[n - 1][i]
        max_visible_height_right = matrix[i][n - 1]

        for j in range(1, n - 1):
            if matrix[i][n - j - 1] > max_visible_height_right:
                coord = (i, n - j - 1)
                max_visible_height_right = matrix[i][n - j - 1]
                visited.add(coord)

            if matrix[n - 1 - j][i] > max_visible_height_bottom:
                coord = (n - 1 - j, i)
                max_visible_height_bottom = matrix[n - 1 - j][i]
                visited.add(coord)

            if matrix[j][i] > max_visible_height_top:
                coord = (j, i)
                max_visible_height_top = matrix[j][i]
                count += 1
                visited.add(coord)

            if matrix[i][j] > max_visible_height_left:
                coord = (i, j)
                count += 1
                max_visible_height_left = matrix[i][j]
                visited.add(coord)

    return len(visited) + 2 * m + 2 * (n - 2)


def scenic_score(matrix):
    m = len(matrix)
    n = len(matrix[0])

    def can_move(row, col):
        return row >= 0 and col >= 0 and row < m and col < n

    def get_score(row, col):

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        print('Tree', (row, col), matrix[row][col])
        score = 1

        for direction in directions:
            counter = 0
            next_row = row
            next_col = col
            height = matrix[next_row][next_col]

            if (1, 0) == direction:
                print('going right')
            if (0, 1) == direction:
                print('going down')
            if (-1, 0) == direction:
                print('going left')
            if (0, -1) == direction:
                print('going up')

            while True:
                x, y = direction
                next_col += x
                next_row += y
                if not can_move(next_row, next_col):
                    break

                counter += 1
                if height <= matrix[next_row][next_col]:
                    break

                # height = matrix[next_row][next_col]
                # print('Current height', height, 'next height',
                #       matrix[next_row][next_col])

            print('I can see ', counter, 'trees')
            score *= counter
        return score

    def calc():
        scenic_score = 0
        coord = None
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                score = get_score(i, j)
                if score > scenic_score:
                    scenic_score = score
                    coord = (i, j)
                scenic_score = max(scenic_score, get_score(i, j))
        print('highest coord', coord)
        return scenic_score
    return calc()


matrix = build_matrix(lines)
print('matrix', matrix)
print(count_visible_trees(matrix))
print('higheest score', scenic_score(matrix))

file.close()
