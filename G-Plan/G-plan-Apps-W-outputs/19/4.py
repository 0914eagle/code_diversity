_shortest_sequence(N, M, S):
    game_over = [i for i, val in enumerate(S) if val == '1']
    dp = [-1] * (N + 1)
    dp[0] = 0
    prev = [-1] * (N + 1)
    
    for i in range(N + 1):
        if dp[i] == -1:
            continue
        for j in range(1, M + 1):
            if i + j > N:
                break
            if i + j in game_over:
                continue
            if dp[i + j] == -1 or dp[i] + 1 < dp[i + j]:
                dp[i + j] = dp[i] + 1
                prev[i + j] = i
    
    if dp[N] == -1:
        return -1
    
    result = []
    while N > 0:
        result.append(N - prev[N])
        N = prev[N]
    
    return ' '.join(map(str, result[::-1]))


if __name__ == "__main__":
    N, M = map(int, input().split())
    S = input().strip()
    
    result = find_shortest_sequence(N, M, S)
    print(result