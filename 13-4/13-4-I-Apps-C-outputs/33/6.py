
def f1(N, M, ps):
    # Calculate the probability of Anthony winning the game
    p = 0
    for i in range(N+M-1):
        p += ps[i] * (1 - ps[i]) ** (N+M-2-i)
    return p

def f2(N, M, ps):
    # Calculate the probability of Cora winning the game
    p = 1 - f1(N, M, ps)
    return p

if __name__ == '__main__':
    N, M = map(int, input().split())
    ps = []
    for i in range(N+M-1):
        ps.append(float(input()))
    print(f1(N, M, ps))

