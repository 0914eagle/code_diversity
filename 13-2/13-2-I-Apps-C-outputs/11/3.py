
def is_valid_magic_checkerboard(checkerboard):
    n, m = len(checkerboard), len(checkerboard[0])
    for i in range(n):
        for j in range(m):
            if checkerboard[i][j] == 0:
                return False
    for i in range(n):
        for j in range(m-1):
            if checkerboard[i][j] > checkerboard[i][j+1]:
                return False
    for j in range(m):
        for i in range(n-1):
            if checkerboard[i][j] > checkerboard[i+1][j]:
                return False
    for i in range(n-1):
        for j in range(m-1):
            if checkerboard[i][j] == checkerboard[i+1][j+1]:
                return False
    return True

def fill_magic_checkerboard(checkerboard):
    n, m = len(checkerboard), len(checkerboard[0])
    for i in range(n):
        for j in range(m):
            if checkerboard[i][j] == 0:
                checkerboard[i][j] = 1
    for i in range(n):
        for j in range(m-1):
            if checkerboard[i][j] > checkerboard[i][j+1]:
                checkerboard[i][j], checkerboard[i][j+1] = checkerboard[i][j+1], checkerboard[i][j]
    for j in range(m):
        for i in range(n-1):
            if checkerboard[i][j] > checkerboard[i+1][j]:
                checkerboard[i][j], checkerboard[i+1][j] = checkerboard[i+1][j], checkerboard[i][j]
    for i in range(n-1):
        for j in range(m-1):
            if checkerboard[i][j] == checkerboard[i+1][j+1]:
                checkerboard[i][j], checkerboard[i+1][j+1] = checkerboard[i+1][j+1], checkerboard[i][j]
    return checkerboard

def get_sum(checkerboard):
    return sum(sum(row) for row in checkerboard)

def solve(checkerboard):
    if not is_valid_magic_checkerboard(checkerboard):
        return -1
    filled_checkerboard = fill_magic_checkerboard(checkerboard)
    return get_sum(filled_checkerboard)

if __name__ == '__main__':
    checkerboard = [[1, 2, 3, 0], [0, 0, 5, 6], [0, 0, 7, 8], [7, 0, 0, 10]]
    print(solve(checkerboard))

