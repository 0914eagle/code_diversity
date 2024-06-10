test_sequence_to_win(N, M, S):
    game_over = [i for i, val in enumerate(S) if val == '1']
    dp = [-1] * (N + 1)
    dp[0] = []
    queue = [(0, [])]

    while queue:
        square, seq = queue.pop(0)
        for move in range(1, M + 1):
            next_square = square + move
            if next_square > N:
                continue
            if next_square in game_over:
                continue
            if dp[next_square] == -1 or len(seq + [move]) < len(dp[next_square]):
                dp[next_square] = seq + [move]
                queue.append((next_square, seq + [move]))

    if dp[N] == -1:
        return -1
    return dp[N]


if __name__ == '__main__':
    N, M = map(int, input().split())
    S = input().strip()
    result = shortest_sequence_to_win(N, M, S)
    if result == -1:
        print(-1)
    else:
        print(*result