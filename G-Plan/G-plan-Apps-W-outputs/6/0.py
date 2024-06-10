k_corner_inversion(a, b, n, m, i, j):
    if a[i][j] != b[i][j]:
        if i + 1 < n and j + 1 < m:
            a[i][j] = 1 - a[i][j]
            a[i + 1][j] = 1 - a[i + 1][j]
            a[i][j + 1] = 1 - a[i][j + 1]
            a[i + 1][j + 1] = 1 - a[i + 1][j + 1]
        else:
            return False
    return True

def matrix_transformation_check(a, b, n, m):
    for i in range(n):
        for j in range(m):
            if not check_corner_inversion(a, b, n, m, i, j):
                return "No"
    return "Yes"

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    b = [list(map(int, input().split())) for _ in range(n)]
    
    result = matrix_transformation_check(a, b, n, m)
    print(result)
