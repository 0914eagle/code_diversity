
def get_minimum_penalty(n, m, k):
    # Initialize the matrix with 0s
    matrix = [[0] * m for _ in range(n)]
    
    # Initialize the penalty to 0
    penalty = 0
    
    # Loop through each candy
    for i in range(k):
        # Choose the cell for the candy
        row, col = choose_cell(matrix)
        
        # Update the matrix with the candy
        matrix[row][col] = i + 1
        
        # Calculate the penalty for the candy
        penalty += calculate_penalty(matrix, row, col)
    
    return penalty

def choose_cell(matrix):
    # Find the first empty cell in the matrix
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                return row, col
    
    # If no empty cell is found, return the last cell
    return len(matrix) - 1, len(matrix[0]) - 1

def calculate_penalty(matrix, row, col):
    # Initialize the penalty to 0
    penalty = 0
    
    # Calculate the penalty for the candy
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0 and abs(i - row) + abs(j - col) == 1:
                penalty += 1
    
    return penalty

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    print(get_minimum_penalty(n, m, k))

