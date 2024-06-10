
def is_possible(A, B, C):
    dp = [False] * B
    dp[0] = True

    for i in range(1, B):
        if dp[i - A]:
            dp[i] = True

    return "YES" if dp[C] else "NO"

if __name__ == "__main__":
    A, B, C = map(int, input().split())
    print(is_possible(A, B, C))
