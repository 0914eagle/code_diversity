
def get_max_sum(sequence):
    n = len(sequence)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + sequence[i - 1])
    return dp[n]

def solve(sequence):
    n = len(sequence)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + sequence[i - 1])
    return dp[n]

if __name__ == '__main__':
    n = int(input())
    sequence = list(map(int, input().split()))
    print(solve(sequence))

