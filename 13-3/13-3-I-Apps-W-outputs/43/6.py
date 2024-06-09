
def is_good_matrix(matrix):
    # Check if the matrix is good
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    if matrix[k][l] == 1:
                        break
                else:
                    break
            else:
                break
        else:
            break
    else:
        return True
    return False

def make_good_matrix(matrix):
    # Check if the matrix is already good
    if is_good_matrix(matrix):
        return matrix
    
    # Find the first row and column with a zero
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                break
        else:
            continue
        break
    
    # Flip the zero to a one
    matrix[i][j] = 1
    
    # Return the modified matrix
    return matrix

def solve(matrix):
    # Check if the matrix is good
    if is_good_matrix(matrix):
        return 0
    
    # Make a copy of the matrix
    matrix_copy = [row[:] for row in matrix]
    
    # Make the matrix good
    make_good_matrix(matrix_copy)
    
    # Count the number of cells changed
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != matrix_copy[i][j]:
                count += 1
    
    # Return the number of cells changed
    return count

if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input())))
    print(solve(matrix))

