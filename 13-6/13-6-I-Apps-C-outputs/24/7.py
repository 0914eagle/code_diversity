
def get_input():
    n, m = map(int, input().split())
    mark = [input() for _ in range(n)]
    return n, m, mark

def get_stamp_size(mark):
    stamp_size = 0
    for row in mark:
        for cell in row:
            if cell == '#':
                stamp_size += 1
    return stamp_size

def get_min_nubs(mark):
    n, m, mark = get_input()
    stamp_size = get_stamp_size(mark)
    min_nubs = 0
    for i in range(n - 1):
        for j in range(m - 1):
            if mark[i][j] == '#' and mark[i + 1][j] == '#' and mark[i][j + 1] == '#' and mark[i + 1][j + 1] == '#':
                min_nubs = max(min_nubs, stamp_size)
    return min_nubs

def main():
    print(get_min_nubs())

if __name__ == '__main__':
    main()

