
def get_input():
    n, m = map(int, input().split())
    mark = [input() for _ in range(n)]
    return n, m, mark

def count_nubs(mark):
    nubs = 0
    for row in mark:
        for cell in row:
            if cell == '#':
                nubs += 1
    return nubs

def get_min_nubs(mark):
    n, m, mark = get_input()
    nubs = count_nubs(mark)
    if nubs % 2 == 0:
        return nubs // 2
    else:
        return (nubs // 2) + 1

if __name__ == '__main__':
    print(get_min_nubs())

