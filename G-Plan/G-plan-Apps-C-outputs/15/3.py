
def count_nubs(n, m, mark):
    nubs = set()
    for i in range(n):
        for j in range(m):
            if mark[i][j] == '#':
                nubs.add((i, j))
    return len(nubs)

if __name__ == "__main__":
    n, m = map(int, input().split())
    mark = [input() for _ in range(n)]
    result = count_nubs(n, m, mark)
    print(result)
