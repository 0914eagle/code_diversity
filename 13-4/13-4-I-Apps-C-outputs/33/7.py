
def f1(N, M, ps):
    # Calculate the probability of Anthony winning the game
    p_win = 0
    for i in range(N+M-1):
        p_win += ps[i] * (1 - ps[i]) ** (N+M-2-i)
    return p_win

def f2(N, M, ps):
    # Calculate the probability of Cora winning the game
    p_lose = 0
    for i in range(N+M-1):
        p_lose += (1 - ps[i]) * ps[i] ** (N+M-2-i)
    return p_lose

def f3(N, M, ps):
    # Calculate the probability of Anthony winning the game
    p_win = f1(N, M, ps)
    # Calculate the probability of Cora winning the game
    p_lose = f2(N, M, ps)
    # Return the probability of Anthony winning the game
    return p_win / (p_win + p_lose)

if __name__ == '__main__':
    N, M = map(int, input().split())
    ps = []
    for i in range(N+M-1):
        ps.append(float(input()))
    print(f3(N, M, ps))

