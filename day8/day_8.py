import time


def build_forest(lines):
    forest = []
    for line in lines:
        line = line.strip()
        row = [int(s) for s in list(line)]
        forest.append(row)

    return forest


def count_visible_trees(forest):
    n = len(forest)
    visited = set()

    for i in range(1, n - 1):
        max_visible_height_top = forest[0][i]
        max_visible_height_left = forest[i][0]
        max_visible_height_bottom = forest[n - 1][i]
        max_visible_height_right = forest[i][n - 1]

        for j in range(1, n - 1):
            if forest[i][n - j - 1] > max_visible_height_right:
                coord = (i, n - j - 1)
                max_visible_height_right = forest[i][n - j - 1]
                visited.add(coord)

            if forest[n - 1 - j][i] > max_visible_height_bottom:
                coord = (n - 1 - j, i)
                max_visible_height_bottom = forest[n - 1 - j][i]
                visited.add(coord)

            if forest[j][i] > max_visible_height_top:
                coord = (j, i)
                max_visible_height_top = forest[j][i]
                visited.add(coord)

            if forest[i][j] > max_visible_height_left:
                coord = (i, j)
                max_visible_height_left = forest[i][j]
                visited.add(coord)

    return len(visited) + 4 * (n - 1)


def scenic_score(forest):
    n = len(forest)

    def can_move(row, col):
        return row >= 0 and col >= 0 and row < n and col < n

    def get_score(row, col) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        score = 1
        for direction in directions:
            counter = 0
            next_row = row
            next_col = col
            height = forest[next_row][next_col]
            while True:
                x, y = direction
                next_col += x
                next_row += y
                if not can_move(next_row, next_col):
                    break

                counter += 1
                if height <= forest[next_row][next_col]:
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


file = open('day8/input.txt', 'r')
lines = file.readlines()
file.close()

forest = build_forest(lines)

print('First', count_visible_trees(forest))
start_time = time.time()
print('Second', scenic_score(forest))
end_time = time.time()
time_elapsed = end_time - start_time
print('Time elapsed', time_elapsed * 1000)

# file.close()
