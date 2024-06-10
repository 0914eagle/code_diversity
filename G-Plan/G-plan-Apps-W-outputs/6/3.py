k_submatrix(a, b, x, y):
    return a[x][y] == b[x][y] and a[x+1][y] == b[x+1][y] and a[x][y+1] == b[x][y+1] and a[x+1][y+1] == b[x+1][y+1]

def transform_possible(a, b, n, m):
    for i in range(n-1):
        for j in range(m-1):
            if not check_submatrix(a, b, i, j):
                a[i][j] = 1 - a[i][j]
                a[i+1][j] = 1 - a[i+1][j]
                a[i][j+1] = 1 - a[i][j+1]
                a[i+1][j+1] = 1 - a[i+1][j+1]
                if not check_submatrix(a, b, i, j):
                    return "No"
    return "Yes"

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    b = [list(map(int, input().split())) for _ in range(n)]
    print(transform_possible(a, b, n, m))
