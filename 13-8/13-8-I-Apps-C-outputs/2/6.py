
def get_largest_square_killer(matrix):
    # Initialize a list to store the sizes of all square killers
    killer_sizes = []
    
    # Loop through each row of the matrix
    for row in range(len(matrix)):
        # Loop through each column of the matrix
        for col in range(len(matrix[0])):
            # Check if the current cell is part of a square killer
            if is_square_killer(matrix, row, col):
                # If it is, add the size of the killer to the list
                killer_sizes.append(get_killer_size(matrix, row, col))
    
    # Return the largest killer size, or -1 if there are no square killers
    return max(killer_sizes) if killer_sizes else -1

def is_square_killer(matrix, row, col):
    # Check if the current cell is part of a square killer
    return matrix[row][col] == "1" and \
           matrix[row][col + 1] == "1" and \
           matrix[row][col + 2] == "1" and \
           matrix[row + 1][col] == "1" and \
           matrix[row + 1][col + 1] == "1" and \
           matrix[row + 1][col + 2] == "1" and \
           matrix[row + 2][col] == "1" and \
           matrix[row + 2][col + 1] == "1" and \
           matrix[row + 2][col + 2] == "1"

def get_killer_size(matrix, row, col):
    # Find the size of the square killer by checking the number of consecutive "1"s in the row and column
    row_size = 1
    while row + row_size < len(matrix) and matrix[row + row_size][col] == "1":
        row_size += 1
    
    col_size = 1
    while col + col_size < len(matrix[0]) and matrix[row][col + col_size] == "1":
        col_size += 1
    
    return min(row_size, col_size)

def main():
    # Read the input matrix
    R, C = map(int, input().split())
    matrix = [input() for _ in range(R)]
    
    # Find the largest square killer
    largest_square_killer = get_largest_square_killer(matrix)
    
    # Print the result
    print(largest_square_killer)

if __name__ == '__main__':
    main()

