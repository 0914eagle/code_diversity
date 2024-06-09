
def is_magic_checkerboard(checkerboard):
    n, m = len(checkerboard), len(checkerboard[0])
    for i in range(n):
        for j in range(m):
            if checkerboard[i][j] == 0:
                return False
    for i in range(n):
        for j in range(m):
            if i > 0 and checkerboard[i][j] == checkerboard[i-1][j]:
                return False
            if j > 0 and checkerboard[i][j] == checkerboard[i][j-1]:
                return False
    for i in range(n-1):
        for j in range(m-1):
            if checkerboard[i][j] == checkerboard[i+1][j] or checkerboard[i][j] == checkerboard[i][j+1]:
                return False
    return True

def fill_magic_checkerboard(checkerboard):
    n, m = len(checkerboard), len(checkerboard[0])
    for i in range(n):
        for j in range(m):
            if checkerboard[i][j] == 0:
                checkerboard[i][j] = 1
    for i in range(n):
        for j in range(m):
            if i > 0 and checkerboard[i][j] == checkerboard[i-1][j]:
                checkerboard[i][j] += 1
            if j > 0 and checkerboard[i][j] == checkerboard[i][j-1]:
                checkerboard[i][j] += 1
    for i in range(n-1):
        for j in range(m-1):
            if checkerboard[i][j] == checkerboard[i+1][j] or checkerboard[i][j] == checkerboard[i][j+1]:
                checkerboard[i][j] += 1
    return checkerboard

def get_min_sum(checkerboard):
    n, m = len(checkerboard), len(checkerboard[0])
    min_sum = 0
    for i in range(n):
        for j in range(m):
            min_sum += checkerboard[i][j]
    return min_sum

def solve(checkerboard):
    if is_magic_checkerboard(checkerboard):
        return get_min_sum(checkerboard)
    else:
        filled_checkerboard = fill_magic_checkerboard(checkerboard)
        if is_magic_checkerboard(filled_checkerboard):
            return get_min_sum(filled_checkerboard)
        else:
            return -1

if __name__ == '__main__':
    checkerboard = [[1, 2, 3, 0], [0, 0, 5, 6], [0, 0, 7, 8], [7, 0, 0, 10]]
    print(solve(checkerboard))

