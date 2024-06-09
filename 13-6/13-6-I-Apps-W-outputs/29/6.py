
def read_input():
    N, C = map(int, input().split())
    D = [[0] * (C + 1) for _ in range(C + 1)]
    for i in range(1, C + 1):
        D[i] = list(map(int, input().split()))
    c = []
    for i in range(N):
        c.append(list(map(int, input().split())))
    return N, C, D, c

def get_wrongness(c, D):
    wrongness = 0
    for i in range(len(c)):
        for j in range(len(c[0])):
            if c[i][j] != c[(i + j) % 3][(j + i) % 3]:
                wrongness += D[c[i][j]][c[(i + j) % 3][(j + i) % 3]]
    return wrongness

def repaint(c, D):
    N = len(c)
    for i in range(N):
        for j in range(N):
            if c[i][j] != c[(i + j) % 3][(j + i) % 3]:
                c[i][j] = c[(i + j) % 3][(j + i) % 3]
    return c, get_wrongness(c, D)

def solve(N, C, D, c):
    wrongness = get_wrongness(c, D)
    min_wrongness = wrongness
    while True:
        c, wrongness = repaint(c, D)
        if wrongness < min_wrongness:
            min_wrongness = wrongness
        else:
            break
    return min_wrongness

if __name__ == '__main__':
    N, C, D, c = read_input()
    print(solve(N, C, D, c))

