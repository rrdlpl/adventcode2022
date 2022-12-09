import matplotlib.pyplot as plt
from matplotlib import animation

import math
import time

# print(math.dist([0, 2], [2, 2]))

moves = {
    'R': (1, 0),
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0)
}


def simulate(lines: str):
    head = (0, 0)
    tail = (0, 0)
    path = []
    visited = set()
    visited.add(tail)

    for line in lines:
        line = line.strip()
        instruction, n = line.split()

        for _ in range(int(n)):
            x, y = head
            x += moves[instruction][0]
            y += moves[instruction][1]

            head = (x, y)
            if math.dist(tail, head) >= 2.0:
                tail = path[-1]
                visited.add(tail)
            path.append(head)

    return visited

# stupid rope doesnt move diagonally
# def simulate2(lines: str):
#     rope = [(0, 0) for _ in range(10)]
#     tail = rope[0]
#     visited = set()
#     visited.add(tail)

#     for line in lines:
#         line = line.strip()
#         instruction, n = line.split()
#         head = rope[-1]
#         # print('Instruction', instruction)
#         # print('Head at', head)
#         for _ in range(int(n)):
#             x, y = head
#             dx = moves[instruction][0]
#             dy = moves[instruction][1]
#             x += dx
#             y += dy
#             head = (x, y)
#             rope[-1] = (x, y)
#             for i in range(len(rope) - 2, -1, -1):
#                 prev = rope[i]
#                 h = rope[i + 1]
#                 prev_x, prev_y = prev

#                 if math.dist(h, prev) >= 2.0:
#                     rope[i] = (prev_x + dx, prev_y + dy)

#             print(rope)
#             visited.add(rope[0])

#     return visited


def simulate2(lines: str):
    rope = [(0, 0) for _ in range(10)]
    tail = rope[0]
    visited = set()
    visited.add(tail)
    paths = []
    paths.append(rope.copy())

    for line in lines:
        line = line.strip()
        instruction, n = line.split()
        head = rope[-1]
        # print('Instruction', instruction)
        # print('Head at', head)
        for _ in range(int(n)):
            x, y = head
            x += moves[instruction][0]
            y += moves[instruction][1]
            head = (x, y)
            rope[-1] = (x, y)
            for i in range(len(rope) - 2, -1, -1):
                prev = rope[i]
                h = rope[i + 1]
                h_x, h_y = h
                prev_x, prev_y = prev

                if math.dist(h, prev) >= 2.0:
                    if h_x > prev_x:
                        prev_x += 1
                    elif h_x < prev_x:
                        prev_x -= 1
                    if h_y > prev_y:
                        prev_y += 1
                    elif h_y < prev_y:
                        prev_y -= 1
                    rope[i] = (prev_x, prev_y)

            print(rope)
            paths.append(rope.copy())
            visited.add(rope[0])

    return (visited, paths)


file = open('day9/input.txt', 'r')
lines = file.readlines()

start_time = time.time()

solution1 = simulate(lines)
print('Solution 1', len(solution1))
visited, paths = simulate2(lines)

print('Solution 2', len(visited))
end_time = time.time()
print('Time ellapsed', (end_time - start_time) * 1000)

file.close()

# print('paths', paths)

# Create some data to plot
x = []
y = []
for path in paths:
    for coord in path:
        x.append(coord[0])
        y.append(coord[1])




# Create a figure and axis
fig, ax = plt.subplots()

# Create a scatter plot
scatter, = ax.plot(x, y, 'bo')

# This function will be called to update the plot
def update(num):
    # Update the data for the scatter plot
    scatter.set_data(x[num-10:num], y[num-10:num])
    colors = ['crimson', 'darkorange', 'lime', 'cornflowerblue', 'purple', 'fuchsia']
    scatter.set_color(colors[num % len(colors)])

    
    return scatter,

# Create the animation
plt.axis([min(x) - 10, max(x) + 10, min(y) - 10, max(y) + 10])

anim = animation.FuncAnimation(fig, update, frames=len(x), interval=100)
# FFwriter=animation.FFMpegWriter(fps=10, extra_args=['-vcodec', 'libx264'])

anim.save('my_animation2.gif', fps=30)

# Show the plot
plt.show()