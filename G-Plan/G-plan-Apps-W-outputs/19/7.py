_winning_sequence(N, M, S):
    if S[0] == '1' or S[N] == '1':
        return "-1"

    dp = [-1] * (N + 1)
    dp[0] = 0
    prev = [-1] * (N + 1)

    for i in range(N):
        if S[i] == '1':
            continue

        for j in range(1, M + 1):
            if i + j > N:
                break

            if dp[i + j] == -1 or dp[i + j] > dp[i] + 1:
                dp[i + j] = dp[i] + 1
                prev[i + j] = j

    if dp[N] == -1:
        return "-1"

    result = []
    idx = N
    while idx > 0:
        result.append(prev[idx])
        idx -= prev[idx]

    return " ".join(map(str, result))


if __name__ == "__main__":
    N, M = map(int, input().split())
    S = input().strip()
    print(find_winning_sequence(N, M, S)