import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict
import heapq as heap

import math
import time
import numpy as np


file = open('day12/input.txt', 'r')
lines = file.readlines()


def generate_matrix(lines):
    matrix = []
    for line in lines:
        line = line.strip()
        matrix.append(list(line))

    return matrix


def get_start_and_end_points(matrix):
    start = end = None
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'S':
                start = (i, j)
            if matrix[i][j] == 'E':
                end = (i, j)
            if start and end:
                break
    return (start, end)


def dijkstra(matrix, start, end):
    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0
    visited = set()
    queue = []
    path = {}
    heap.heappush(queue, (0, start))
    matrix[start[0]][start[1]] = 'a'
    matrix[end[0]][end[1]] = 'z'

    def get_adjacent_nodes(node):
        # directions: U, R, D, L
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        adjacents = []
        row, col = node
        for direction in directions:
            x, y = direction
            new_col = col + x
            new_row = row + y
            old_index = ord(matrix[row][col])
            # Can hike ? (abs(old_index - ord(matrix[new_row][new_col]) <= 1
            # They can jump to suicide =>  old_index >= ord(matrix[new_row][new_col])
            if new_col >= 0 and new_row >= 0 and new_col < len(matrix[0]) and new_row < len(matrix) and can_jump_or_hike(new_col, new_row, old_index):
                adjacents.append((new_row, new_col))
        return adjacents

    def can_jump_or_hike(new_col, new_row, old_index):
        return (abs(old_index - ord(matrix[new_row][new_col])) <= 1 or old_index >= ord(matrix[new_row][new_col]))

    while queue:
        _, node = heap.heappop(queue)
        visited.add(node)

        adjacents = get_adjacent_nodes(node)
        for adj_node in adjacents:
            if adj_node in visited:
                continue
            new_steps = distances[node] + 1
            if new_steps < distances[adj_node]:
                distances[adj_node] = new_steps
                path[adj_node] = node
                heap.heappush(queue, (new_steps, adj_node))

    return (distances[end], path)


def dijkstra_2(matrix, start, end):
    distances = defaultdict(lambda: float('inf'))
    distances[end] = 0
    visited = set()
    queue = []
    path = {}
    heap.heappush(queue, (0, end))
    matrix[start[0]][start[1]] = 'a'
    matrix[end[0]][end[1]] = 'z'

    def get_adjacent_nodes(node):
        # directions: U, R, D, L
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        adjacents = []
        row, col = node
        for direction in directions:
            x, y = direction
            new_col = col + x
            new_row = row + y
            old_index = ord(matrix[row][col])

            if new_col >= 0 and new_row >= 0 and new_col < len(matrix[0]) and new_row < len(matrix) and can_jump_or_hike(new_col, new_row, old_index):
                adjacents.append((new_row, new_col))
        return adjacents

    def can_jump_or_hike(new_col, new_row, old_index):
        return (abs(ord(matrix[new_row][new_col]) - old_index) <= 1 or old_index <= ord(matrix[new_row][new_col]))

    while queue:
        _, node = heap.heappop(queue)
        visited.add(node)

        adjacents = get_adjacent_nodes(node)
        for adj_node in adjacents:
            if adj_node in visited:
                continue
            new_steps = distances[node] + 1
            if new_steps < distances[adj_node]:
                path[adj_node] = node
                distances[adj_node] = new_steps
                heap.heappush(queue, (new_steps, adj_node))

    min_steps = math.inf
    new_start = None
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'a':
                if distances[(i, j)] < min_steps:
                    min_steps = distances[(i, j)]
                    new_start = (i, j)
    return min_steps, path, new_start


start_time = time.time()

matrix = generate_matrix(lines)
start, end = get_start_and_end_points(matrix)

end_steps, first_part_path = dijkstra(matrix, start, end)
print('Solution 1', end_steps)

min_steps, second_path, new_start = dijkstra_2(matrix, start, end)
print('Solution 2', min_steps)

print('Start ', start, 'End', end)
end_time = time.time()
print('Time ellapsed', (end_time - start_time) * 1000)

file.close()


# Create a grid of points using the meshgrid function
x, y = np.meshgrid(np.arange(0, 10), np.arange(0, 10))


def heatmap(matrix):
    heatmap = []
    for row in matrix:
        heatmap.append([ord(s) - ord('a') for s in row])
    return heatmap


heat = heatmap(matrix)


def draw_path(start, end, path, heat):
    ax = sns.heatmap(heat, cmap="YlGnBu")

    print('Start', start)
    print('End', end)
    print('Path end', path[end])
    c = 1
    while path[end] != start:
        c += 1
        node = path[end]
        i, j = node
        ax.add_artist(plt.Rectangle((j, i), 1, 1, color='red'))
        end = node


#draw_path(start, end, first_part_path, heat)


draw_path(end, new_start, second_path, heat)

plt.show()
