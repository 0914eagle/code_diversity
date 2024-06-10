
def is_possible(A, B, C):
    dp = [False] * B
    dp[0] = True

    for i in range(1, A + 1):
        if dp[C]:
            return "YES"
        new_dp = dp.copy()
        for j in range(B):
            if dp[j]:
                new_dp[(j + i) % B] = True
        dp = new_dp

    return "YES" if dp[C] else "NO"

if __name__ == "__main__":
    A, B, C = map(int, input().split())
    print(is_possible(A, B, C))
