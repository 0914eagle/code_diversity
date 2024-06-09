
def get_input():
    n_r, n_c, n, m = map(int, input().split())
    assert 1 <= n_r <= 10000 and 1 <= n_c <= 10000 and 1 <= n <= 100 and 1 <= m <= 100 and n + m <= 100
    files = []
    for _ in range(n + m):
        r, c = map(int, input().split())
        assert 0 <= r < n_r and 0 <= c < n_c
        files.append((r, c))
    return n_r, n_c, n, m, files

def solve(n_r, n_c, n, m, files):
    # find the bounding box of the files to be deleted
    x1, y1, x2, y2 = float('inf'), float('inf'), float('-inf'), float('-inf')
    for r, c in files[:n]:
        x1 = min(x1, c)
        y1 = min(y1, r)
        x2 = max(x2, c + 9)
        y2 = max(y2, r + 15)

    # find the bounding box of the files that should not be deleted
    x3, y3, x4, y4 = float('inf'), float('inf'), float('-inf'), float('-inf')
    for r, c in files[n:]:
        x3 = min(x3, c)
        y3 = min(y3, r)
        x4 = max(x4, c + 9)
        y4 = max(y4, r + 15)

    # calculate the area of the bounding box of the files to be deleted
    area_to_delete = (x2 - x1) * (y2 - y1)

    # calculate the area of the bounding box of the files that should not be deleted
    area_keep = (x4 - x3) * (y4 - y3)

    # calculate the minimum number of files to move to delete all the appropriate files in one delete operation
    min_moves = 0
    for i in range(n):
        r, c = files[i]
        if x1 <= c + 4.5 and c + 4.5 <= x2 and y1 <= r + 7.5 and r + 7.5 <= y2:
            min_moves += 1

    return min_moves

if __name__ == '__main__':
    n_r, n_c, n, m, files = get_input()
    print(solve(n_r, n_c, n, m, files))

