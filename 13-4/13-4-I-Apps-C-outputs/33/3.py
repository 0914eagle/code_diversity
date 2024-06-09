
def f1(N, M, ps):
    # Calculate the probability of Anthony winning the game
    p_win = 0
    for i in range(N+M-1):
        p_win += ps[i] * (1 - ps[i]) ** (N+M-2-i)
    return p_win

def f2(N, M, ps):
    # Calculate the probability of Anthony winning the game using dynamic programming
    p = [0] * (N+M)
    p[0] = 1
    p[1] = 1 - ps[0]
    for i in range(2, N+M):
        p[i] = p[i-1] * (1 - ps[i-1]) + p[i-2] * ps[i-1]
    return p[N+M-1]

if __name__ == '__main__':
    N, M = map(int, input().split())
    ps = []
    for i in range(N+M-1):
        ps.append(float(input()))
    print(f1(N, M, ps))
    print(f2(N, M, ps))

