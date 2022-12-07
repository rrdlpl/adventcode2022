from collections import deque
import math


file = open('day7/input.txt', 'r')
lines = file.readlines()


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Folder:
    def __init__(self, name, parent=None):
        self.name = name
        self.folders = {}
        self.files = []
        self.parent = parent
        self.files_size = 0

    def add_folder(self, folder):
        self.folders[folder.name] = folder

    def add_file(self, file):
        self.files.append(file)
        self.files_size += file.size

    def get_folder_size(self):
        sum = 0
        for key in self.folders:
            sum += self.folders[key].get_folder_size()
        return sum + self.files_size


def build_tree(lines):
    root = Folder('/', None)
    current_folder = root
    for i in range(1, len(lines)):
        input = lines[i].strip().split()
        if input[0] == '$' and input[1] == 'ls':
            continue
        if input[0] == '$' and input[1] == 'cd':
            if input[2] == '..':
                current_folder = current_folder.parent
            else:
                current_folder = current_folder.folders[input[2]]
        elif input[0] == 'dir':
            current_folder.add_folder(Folder(input[1], current_folder))
        else:
            current_folder.add_file(File(input[1], int(input[0])))

    return root


def get_sum_directories(root):
    queue = deque()
    sum = 0
    queue.append(root)
    while len(queue) > 0:
        top = queue.pop()
        if top.get_folder_size() < 100000:
            sum += top.get_folder_size()
        for key in top.folders:
            queue.append(top.folders[key])
    return sum


def directory_to_delete(root):
    queue = deque()
    space_required = 30000000 - (70000000 - root.get_folder_size())
    sizes = []

    queue.append(root)
    while len(queue) > 0:
        top = queue.pop()
        if top.get_folder_size() >= space_required:
            sizes.append(top.get_folder_size())
        for key in top.folders:
            queue.append(top.folders[key])

    return sorted(sizes)


root = build_tree(lines)
print('folder size <= 100000 ', get_sum_directories(root))
delete = directory_to_delete(root)

print('Solution 2', delete)
file.close()
