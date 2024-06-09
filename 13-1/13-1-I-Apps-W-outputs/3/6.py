
def is_broken(matrix, k):
    for i in range(len(matrix) - k + 1):
        for j in range(len(matrix[0]) - k + 1):
            if all(matrix[i+x][j+y] == 0 for x in range(k) for y in range(k)):
                return True
    return False

def solve(n, m, k, q, broken_pixels):
    matrix = [[1] * m for _ in range(n)]
    for x, y, t in broken_pixels:
        matrix[x-1][y-1] = 0
        if is_broken(matrix, k):
            return t
    return -1

