
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
    # Check if the matrix is good
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
    
    # Recursively call the function to make the matrix good
    return make_good_matrix(matrix)

def main():
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input())))
    print(make_good_matrix(matrix))

if __name__ == '__main__':
    main()

