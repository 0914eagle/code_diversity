k_submatrix(matrix_a, matrix_b, x, y):
    if matrix_a[x][y] != matrix_b[x][y]:
        for i in range(2):
            for j in range(2):
                matrix_a[x + i][y + j] = 1 - matrix_a[x + i][y + j]

def check_transformation_possible(matrix_a, matrix_b):
    n = len(matrix_a)
    m = len(matrix_a[0])

    for i in range(n - 1):
        for j in range(m - 1):
            if matrix_a[i][j] != matrix_b[i][j]:
                check_submatrix(matrix_a, matrix_b, i, j)

    for i in range(n):
        for j in range(m):
            if matrix_a[i][j] != matrix_b[i][j]:
                return "No"
    
    return "Yes"

if __name__ == "__main__":
    n, m = map(int, input().split())
    matrix_a = [list(map(int, input().split())) for _ in range(n)]
    matrix_b = [list(map(int, input().split())) for _ in range(n)]

    result = check_transformation_possible(matrix_a, matrix_b)
    print(result)
