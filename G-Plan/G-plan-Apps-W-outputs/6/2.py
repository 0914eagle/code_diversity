
def can_transform_matrix(n, m, matrix_a, matrix_b):
    def invert_corners(matrix, x1, y1, x2, y2):
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                matrix[i][j] = 1 - matrix[i][j]

    for i in range(n):
        for j in range(m):
            if matrix_a[i][j] != matrix_b[i][j]:
                if i + 1 < n and j + 1 < m:
                    invert_corners(matrix_a, i, j, i + 1, j + 1)
                else:
                    return "No"
    
    return "Yes"

if __name__ == "__main__":
    n, m = map(int, input().split())
    matrix_a = [list(map(int, input().split())) for _ in range(n)]
    matrix_b = [list(map(int, input().split())) for _ in range(n)]
    
    result = can_transform_matrix(n, m, matrix_a, matrix_b)
    print(result)
