
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
    
    # Find the first row and column with a 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                break
        else:
            continue
        break
    
    # Flip the bit at that position
    matrix[i][j] = 1 - matrix[i][j]
    
    # Return the modified matrix
    return matrix

def solve(matrix):
    # Check if the matrix is already good
    if is_good_matrix(matrix):
        return 0
    
    # Find the first row and column with a 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                break
        else:
            continue
        break
    
    # Flip the bit at that position
    matrix[i][j] = 1 - matrix[i][j]
    
    # Recursively call the function to find the minimum number of changes needed
    return 1 + solve(matrix)

if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    print(solve(matrix))

