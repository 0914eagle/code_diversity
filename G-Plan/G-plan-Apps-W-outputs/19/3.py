_winning_sequence(N, M, S):
    game_over = [i for i, val in enumerate(S) if val == '1']
    dp = [-1] * (N + 1)
    dp[0] = []

    queue = [(0, [])]
    while queue:
        current_square, sequence = queue.pop(0)

        if current_square == N:
            return sequence

        for move in range(1, M + 1):
            next_square = current_square + move
            if next_square <= N and next_square not in game_over:
                new_sequence = sequence + [move]
                if dp[next_square] == -1 or len(dp[next_square]) > len(new_sequence):
                    dp[next_square] = new_sequence
                    queue.append((next_square, new_sequence))

    return -1

if __name__ == "__main__":
    N, M = map(int, input().split())
    S = input().strip()

    result = find_winning_sequence(N, M, S)
    if result == -1:
        print(-1)
    else:
        print(*result