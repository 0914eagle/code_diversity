
def get_penalty(n, m, k):
    # Initialize the matrix and the penalty
    matrix = [[0] * m for _ in range(n)]
    penalty = 0

    # Place the candies one by one
    for i in range(k):
        # Find the cell for the current candy
        cell = find_cell(matrix, i + 1)

        # If there is no cell for the current candy, return -1
        if cell is None:
            return -1

        # Place the candy in the current cell
        matrix[cell[0]][cell[1]] = i + 1

        # Find the path for the current candy
        path = find_path(matrix, cell, i + 1)

        # If there is no path for the current candy, return -1
        if path is None:
            return -1

        # Add the path length to the penalty
        penalty += len(path)

    # Return the penalty
    return penalty

def find_cell(matrix, candy):
    # Find an empty cell for the current candy
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                return [i, j]
    return None

def find_path(matrix, cell, candy):
    # Initialize the path and the current cell
    path = []
    current_cell = cell

    # While the current cell is not the starting cell
    while current_cell != [0, 0]:
        # Find the previous cell
        previous_cell = find_previous_cell(matrix, current_cell, candy)

        # If there is no previous cell, return None
        if previous_cell is None:
            return None

        # Add the current cell to the path
        path.append(current_cell)

        # Set the current cell as the previous cell
        current_cell = previous_cell

    # Return the path
    return path[::-1]

def find_previous_cell(matrix, cell, candy):
    # Find the previous cell
    for i in range(cell[0] - 1, cell[0] + 2):
        for j in range(cell[1] - 1, cell[1] + 2):
            if matrix[i][j] == candy and (i, j) != cell:
                return [i, j]
    return None

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    print(get_penalty(n, m, k))

