_winning_sequence(N, M, S):
    game_over = [i for i, val in enumerate(S) if val == '1']
    visited = [False] * (N + 1)
    queue = [(0, [])]

    while queue:
        square, sequence = queue.pop(0)
        if square == N:
            return sequence

        for move in range(1, M + 1):
            next_square = square + move
            if next_square <= N and next_square not in game_over and not visited[next_square]:
                visited[next_square] = True
                queue.append((next_square, sequence + [move]))

    return -1

if __name__ == '__main__':
    N, M = map(int, input().split())
    S = input().strip()
    result = find_winning_sequence(N, M, S)
    if result == -1:
        print(-1)
    else:
        print(*result)
