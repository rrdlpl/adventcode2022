from collections import deque
import math


class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size


class Folder:
    def __init__(self, name: str, parent=None):
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


class Solution:
    def build_tree(self):
        root = Folder('/', None)
        current_folder = root
        file = open('day7/input.txt', 'r')
        lines = file.readlines()
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

        file.close()

        return root

    def get_sum_directories(self, root: Folder, max_size: int) -> int:
        queue = deque()
        sum = 0
        queue.append(root)
        while len(queue) > 0:
            top = queue.pop()
            if top.get_folder_size() < max_size:
                sum += top.get_folder_size()
            for key in top.folders:
                queue.append(top.folders[key])
        return sum

    def directory_to_delete(self, root: Folder, hd_size: int, update_size: int) -> Folder:
        queue = deque()
        space_required = update_size - (hd_size - root.get_folder_size())

        queue.append(root)
        minimum = math.inf
        folder = None

        while len(queue) > 0:
            top = queue.pop()
            if top.get_folder_size() >= space_required:
                if top.get_folder_size() <= minimum:
                    minimum = top.get_folder_size()
                    folder = top
            for key in top.folders:
                queue.append(top.folders[key])
        return folder

    def main(self):
        root = self.build_tree()
        print('Solution 1, folder size <= 100000 ',
              self.get_sum_directories(root, 100000))
        delete = self.directory_to_delete(root, 70000000, 30000000)
        print('Solution 2', delete.name, delete.get_folder_size())


Solution().main()
