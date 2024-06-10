
def can_transform_matrix(n, m, matrix_a, matrix_b):
    def invert_corners(matrix, i, j):
        matrix[i][j] = 1 - matrix[i][j]
        matrix[i+1][j] = 1 - matrix[i+1][j]
        matrix[i][j+1] = 1 - matrix[i][j+1]
        matrix[i+1][j+1] = 1 - matrix[i+1][j+1]

    for i in range(n-1):
        for j in range(m-1):
            if matrix_a[i][j] != matrix_b[i][j]:
                invert_corners(matrix_a, i, j)
                if matrix_a[i][j] != matrix_b[i][j]:
                    return "No"
    
    return "Yes"

if __name__ == "__main__":
    n, m = map(int, input().split())
    matrix_a = [list(map(int, input().split())) for _ in range(n)]
    matrix_b = [list(map(int, input().split())) for _ in range(n)]

    result = can_transform_matrix(n, m, matrix_a, matrix_b)
    print(result)
