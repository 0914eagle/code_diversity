
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
            if checkerboard[i][j] > checkerboard[i+1][j+1]:
                return False
    for i in range(n-1):
        for j in range(m-1):
            if checkerboard[i][j] > checkerboard[i+1][j+1]:
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
            if checkerboard[i][j] > checkerboard[i+1][j+1]:
                checkerboard[i][j], checkerboard[i+1][j+1] = checkerboard[i+1][j+1], checkerboard[i][j]
    for i in range(n-1):
        for j in range(m-1):
            if checkerboard[i][j] > checkerboard[i+1][j+1]:
                checkerboard[i][j], checkerboard[i+1][j+1] = checkerboard[i+1][j+1], checkerboard[i][j]
    return checkerboard

def get_min_sum(checkerboard):
    n, m = len(checkerboard), len(checkerboard[0])
    min_sum = 0
    for i in range(n):
        for j in range(m):
            min_sum += checkerboard[i][j]
    return min_sum

def main():
    n, m = map(int, input().split())
    checkerboard = []
    for i in range(n):
        checkerboard.append(list(map(int, input().split())))
    if is_valid_magic_checkerboard(checkerboard):
        print(get_min_sum(checkerboard))
    else:
        print(-1)

if __name__ == '__main__':
    main()

