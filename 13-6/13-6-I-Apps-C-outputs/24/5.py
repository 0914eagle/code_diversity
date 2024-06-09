
def get_input():
    n, m = map(int, input().split())
    mark = []
    for _ in range(n):
        mark.append(input())
    return n, m, mark

def count_nubs(mark):
    nubs = 0
    for row in mark:
        for cell in row:
            if cell == '#':
                nubs += 1
    return nubs

def find_min_nubs(mark):
    n, m, mark = get_input()
    min_nubs = count_nubs(mark)
    for i in range(n):
        for j in range(m):
            if mark[i][j] == '#':
                mark[i][j] = '.'
                min_nubs = min(min_nubs, count_nubs(mark))
                mark[i][j] = '#'
    return min_nubs

if __name__ == '__main__':
    print(find_min_nubs())

