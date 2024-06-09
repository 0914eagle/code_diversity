
def is_good_matrix(matrix):
    # Check if the matrix is good
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                # Check if the sub-matrix is even length square
                for k in range(i, len(matrix)):
                    for l in range(j, len(matrix[0])):
                        if matrix[k][l] == 1:
                            # Check if the sub-matrix has an odd number of ones
                            if (k-i+1) * (l-j+1) % 2 == 1:
                                return False
    return True

def make_good_matrix(matrix):
    # Check if the matrix is already good
    if is_good_matrix(matrix):
        return matrix
    
    # Find the first cell that needs to be changed
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                # Change the cell to 0 and return the matrix
                matrix[i][j] = 0
                return matrix
    
    # If no cell needs to be changed, return -1
    return -1

def main():
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    print(make_good_matrix(matrix))

if __name__ == '__main__':
    main()

