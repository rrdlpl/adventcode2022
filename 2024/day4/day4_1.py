
file = open('2024/day4/input.txt', 'r')
lines = file.readlines()

matrix = [list(line.strip()) for line in lines]


def part_one(grid, word):
    def get_neighbors():
        return [
            (0, 1),  
            (1, 0),  
            (1, 1),  
            (1, -1), 
            (0, -1), 
            (-1, 0), 
            (-1, 1), 
            (-1, -1) 
        ]
        
    
    directions = get_neighbors()
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    count = 0

    def search_from(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not (0 <= nx < rows and 0 <= ny < cols) or grid[nx][ny] != word[i]:
                return False
        return True

    for row in range(rows):
        for col in range(cols):
            for dx, dy in directions:
                if search_from(row, col, dx, dy):
                    count += 1

    return count

def part_two(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if grid[row][col] != 'A':
                continue
            text_diag1 = grid[row - 1][col - 1] + grid[row][col] + grid[row + 1][col + 1]
            text_diag2 = grid[row - 1][col + 1] + grid[row][col] + grid[row + 1][col - 1]
            
            if (text_diag1 == 'MAS' or text_diag1 == 'SAM') and (text_diag2 == 'MAS' or text_diag2 == 'SAM'):
                count += 1
    return count 
    
print('Solution 1.', part_one(matrix, 'XMAS'))

print('Solution 2. ', part_two(matrix))