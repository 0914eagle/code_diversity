
def is_possible(A, B, C):
    dp = [False] * B
    dp[0] = True

    for i in range(A, B):
        if dp[i % B]:
            dp[C] = True
            break

    return "YES" if dp[C] else "NO"

if __name__ == "__main__":
    A, B, C = map(int, input().split())
    print(is_possible(A, B, C))
