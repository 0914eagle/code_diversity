
def can_transform_matrix(n, m, matrix_a, matrix_b):
    def invert_corners(i, j):
        if i + 1 < n and j + 1 < m:
            matrix_a[i][j] = 1 - matrix_a[i][j]
            matrix_a[i + 1][j] = 1 - matrix_a[i + 1][j]
            matrix_a[i][j + 1] = 1 - matrix_a[i][j + 1]
            matrix_a[i + 1][j + 1] = 1 - matrix_a[i + 1][j + 1]

    for i in range(n):
        for j in range(m):
            if matrix_a[i][j] != matrix_b[i][j]:
                invert_corners(i, j)
                if matrix_a[i][j] != matrix_b[i][j]:
                    return "No"
    return "Yes"

if __name__ == "__main__":
    n, m = map(int, input().split())
    matrix_a = [list(map(int, input().split())) for _ in range(n)]
    matrix_b = [list(map(int, input().split())) for _ in range(n)]
    
    print(can_transform_matrix(n, m, matrix_a, matrix_b))
