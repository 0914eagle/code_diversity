
def is_good_matrix(matrix):
    # Check if the matrix is good
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    if matrix[k][l] == 1:
                        count = 0
                        for m in range(i, k+1):
                            for n in range(j, l+1):
                                if matrix[m][n] == 1:
                                    count += 1
                        if count % 2 == 0:
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
                matrix[i][j] = 0
                if is_good_matrix(matrix):
                    return matrix
                matrix[i][j] = 1
    
    # If no cell can be changed, return -1
    return -1

def main():
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    print(make_good_matrix(matrix))

if __name__ == '__main__':
    main()

