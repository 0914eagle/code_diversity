
def f1(N, M, p_list):
    # Calculate the probability of Anthony winning the game
    prob_win = 0
    for i in range(N+M-1):
        prob_win += p_list[i] * (1 - prob_win) ** (N-1) * (1 - (1 - p_list[i]) ** M)
    return prob_win

def f2(N, M, p_list):
    # Calculate the probability of Anthony losing the game
    prob_lose = 0
    for i in range(N+M-1):
        prob_lose += (1 - p_list[i]) * prob_lose ** (N-1) * (1 - (1 - p_list[i]) ** M)
    return prob_lose

if __name__ == '__main__':
    N, M = map(int, input().split())
    p_list = []
    for i in range(N+M-1):
        p_list.append(float(input()))
    print(f1(N, M, p_list))

