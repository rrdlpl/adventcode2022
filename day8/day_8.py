import time

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
    n = len(matrix)
    visited = set()

    for i in range(1, n - 1):
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
                visited.add(coord)

            if matrix[i][j] > max_visible_height_left:
                coord = (i, j)
                max_visible_height_left = matrix[i][j]
                visited.add(coord)

    return len(visited) + 4 * (n - 1)


def scenic_score(matrix):
    n = len(matrix)

    def can_move(row, col):
        return row >= 0 and col >= 0 and row < n and col < n

    def get_score(row, col) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        score = 1
        for direction in directions:
            counter = 0
            next_row = row
            next_col = col
            height = matrix[next_row][next_col]
            while True:
                x, y = direction
                next_col += x
                next_row += y
                if not can_move(next_row, next_col):
                    break

                counter += 1
                if height <= matrix[next_row][next_col]:
                    break
            score *= counter
        return score

    def calc() -> int:
        scenic_score = 0
        for i in range(1, n - 2):
            for j in range(1, n - 2):
                scenic_score = max(scenic_score, get_score(i, j))
        return scenic_score
    return calc()


matrix = build_matrix(lines)

print(count_visible_trees(matrix))
start_time = time.time()
print('highest score', scenic_score(matrix))
end_time = time.time()
time_elapsed = end_time - start_time
print('time elapsed', time_elapsed * 1000)

file.close()
