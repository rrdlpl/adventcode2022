# my utils functions

# parse source file into a matrix
# each cell is a character
def parse_matrix(lines):
    matrix = []
    for line in lines:
        line = line.strip()
        matrix.append(list(line))
    return matrix


## Top, Right, Bottom, Left
## for matrix we have to invert Y axis
directions_for_matrix = [(0, -1), (1, 0), (0, 1), (-1, 0)]

#Top, Top-Right, Right, Bottom-Right, Bottom, Bottom-Left, Left, Top-Left
## for matrix we have to invert Y axis
directions_for_matrix_with_diagonals = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)] 