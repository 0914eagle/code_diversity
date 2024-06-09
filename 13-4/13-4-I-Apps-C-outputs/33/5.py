
def f1(N, M, p):
    # Calculate the probability of Anthony winning the game
    prob = 0
    for i in range(N+M-1):
        prob += p[i] * (N-i) / (N+M-1)
    return prob

def f2(N, M, p):
    # Calculate the probability of Cora winning the game
    prob = 0
    for i in range(N+M-1):
        prob += (1-p[i]) * (M-i) / (N+M-1)
    return prob

def f3(N, M, p):
    # Calculate the probability of Anthony winning the game
    prob = f1(N, M, p)
    # Calculate the probability of Cora winning the game
    prob_cora = f2(N, M, p)
    # Return the probability of Anthony winning the game
    return prob / (prob + prob_cora)

if __name__ == '__main__':
    N, M = map(int, input().split())
    p = []
    for i in range(N+M-1):
        p.append(float(input()))
    print(f3(N, M, p))

