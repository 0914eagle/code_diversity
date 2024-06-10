k_transformation_possible(matrix_a, matrix_b):
    n = len(matrix_a)
    m = len(matrix_a[0])
    
    for i in range(n):
        for j in range(m):
            if matrix_a[i][j] != matrix_b[i][j]:
                if not invert_corners(matrix_a, i, j):
                    return "No"
    
    return "Yes"

def invert_corners(matrix, i, j):
    n = len(matrix)
    m = len(matrix[0])
    
    if i + 1 < n and j + 1 < m:
        matrix[i][j] = 1 - matrix[i][j]
        matrix[i+1][j] = 1 - matrix[i+1][j]
        matrix[i][j+1] = 1 - matrix[i][j+1]
        matrix[i+1][j+1] = 1 - matrix[i+1][j+1]
        return True
    
    return False

if __name__ == "__main__":
    n, m = map(int, input().split())
    
    matrix_a = [list(map(int, input().split())) for _ in range(n)]
    matrix_b = [list(map(int, input().split())) for _ in range(n)]
    
    print(check_transformation_possible(matrix_a, matrix_b))
