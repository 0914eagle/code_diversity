
def get_penalty(n, m, k):
    # Initialize the matrix and the penalty
    matrix = [[0] * m for _ in range(n)]
    penalty = 0

    # Place the candies one by one
    for i in range(k):
        # Find the cell for the candy
        cell = find_cell(matrix, i + 1)

        # Place the candy in the cell
        matrix[cell[0]][cell[1]] = i + 1

        # Find the path for the candy
        path = find_path(matrix, cell, i + 1)

        # Add the path length to the penalty
        penalty += len(path)

    return penalty

def find_cell(matrix, candy):
    # Find the first empty cell in the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                return [i, j]

    # If all the cells are taken, return a random cell
    return [random.randint(0, len(matrix) - 1), random.randint(0, len(matrix[0]) - 1)]

def find_path(matrix, cell, candy):
    # Initialize the path and the current cell
    path = []
    current_cell = cell

    # While the current cell is not the first cell
    while current_cell != [0, 0]:
        # Find the previous cell in the path
        previous_cell = find_previous_cell(matrix, current_cell, candy)

        # Add the previous cell to the path
        path.append(previous_cell)

        # Set the current cell to the previous cell
        current_cell = previous_cell

    # Return the path in reverse order
    return path[::-1]

def find_previous_cell(matrix, current_cell, candy):
    # Find the previous cell in the path
    for i in range(current_cell[0] - 1, -1, -1):
        for j in range(current_cell[1] - 1, -1, -1):
            if matrix[i][j] == candy:
                return [i, j]

    for i in range(current_cell[0] + 1, len(matrix)):
        for j in range(current_cell[1] - 1, -1, -1):
            if matrix[i][j] == candy:
                return [i, j]

    for i in range(current_cell[0] - 1, -1, -1):
        for j in range(current_cell[1] + 1, len(matrix[0])):
            if matrix[i][j] == candy:
                return [i, j]

    for i in range(current_cell[0] + 1, len(matrix)):
        for j in range(current_cell[1] + 1, len(matrix[0])):
            if matrix[i][j] == candy:
                return [i, j]

    # If there is no previous cell, return the current cell
    return current_cell

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    print(get_penalty(n, m, k))

