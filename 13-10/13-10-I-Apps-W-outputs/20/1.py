
def find_subsequence(sequence):
    n = len(sequence)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + sequence[i - 1]
    return dp

def find_maximum_subsequence(sequence):
    n = len(sequence)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = max(dp[i - 1] + sequence[i - 1], dp[i - 1])
    return dp

def solve(sequence):
    dp = find_subsequence(sequence)
    maximum = find_maximum_subsequence(sequence)
    return maximum[n]

if __name__ == '__main__':
    n = int(input())
    sequence = list(map(int, input().split()))
    print(solve(sequence))

