
def is_good_matrix(matrix):
    # Check if the matrix is good
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # Check if the sub-matrix is even length square
            if (i + j) % 2 == 0:
                # Count the number of ones in the sub-matrix
                ones = 0
                for k in range(i, i + (j - i) + 1):
                    for l in range(j, j + (k - j) + 1):
                        if matrix[k][l] == 1:
                            ones += 1
                # If the number of ones is not odd, the matrix is not good
                if ones % 2 == 0:
                    return False
    # If all sub-matrices are good, the matrix is good
    return True

def make_good_matrix(matrix):
    # Initialize the number of changes to 0
    changes = 0
    # Loop through each element of the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # If the element is 0 and the sub-matrix is even length square, change it to 1
            if matrix[i][j] == 0 and (i + j) % 2 == 0:
                matrix[i][j] = 1
                changes += 1
    # Return the number of changes
    return changes

def main():
    # Read the input matrix
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    # Check if the matrix is good
    if is_good_matrix(matrix):
        print(-1)
    else:
        # Make the matrix good
        changes = make_good_matrix(matrix)
        print(changes)

if __name__ == '__main__':
    main()

