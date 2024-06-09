
def is_good_matrix(matrix):
    # Check if the matrix is good
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                # Check if the sub-matrix has an odd number of ones
                sub_matrix = get_sub_matrix(matrix, i, j)
                if not is_odd_sub_matrix(sub_matrix):
                    return False
    return True

def get_sub_matrix(matrix, i, j):
    # Get the sub-matrix starting from (i, j)
    sub_matrix = []
    for x in range(i, len(matrix)):
        sub_matrix.append(matrix[x][j:])
    return sub_matrix

def is_odd_sub_matrix(sub_matrix):
    # Check if the sub-matrix has an odd number of ones
    ones = 0
    for row in sub_matrix:
        for elem in row:
            if elem == 1:
                ones += 1
    return ones % 2 == 1

def solve(matrix):
    # Find the minimum number of cells to change to make the matrix good
    min_changes = len(matrix) * len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                # Try changing the cell to 1 and see if the matrix is good
                matrix[i][j] = 1
                if is_good_matrix(matrix):
                    return min_changes
                matrix[i][j] = 0
            else:
                # Try changing the cell to 0 and see if the matrix is good
                matrix[i][j] = 0
                if is_good_matrix(matrix):
                    return min_changes
                matrix[i][j] = 1
    return -1

if __name__ == '__main__':
    matrix = []
    for _ in range(int(input())):
        matrix.append(list(map(int, input().split())))
    print(solve(matrix))

