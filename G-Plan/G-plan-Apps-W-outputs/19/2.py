e_sugoroku(N, M, S):
    if S[0] == '1' or S[N] == '1':
        print(-1)
        return

    dp = [-1] * (N + 1)
    dp[0] = 0
    prev = [-1] * (N + 1)

    for i in range(N):
        if S[i] == '1':
            continue

        for j in range(1, M + 1):
            if i + j <= N and dp[i + j] == -1:
                dp[i + j] = dp[i] + 1
                prev[i + j] = j

    if dp[N] == -1:
        print(-1)
        return

    res = []
    cur = N
    while cur > 0:
        res.append(prev[cur])
        cur -= prev[cur]

    print(*res[::-1])


if __name__ == "__main__":
    N, M = map(int, input().split())
    S = input().strip()
    solve_sugoroku(N, M, S