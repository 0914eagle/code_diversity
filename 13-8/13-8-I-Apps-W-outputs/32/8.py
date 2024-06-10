
def get_total_comfort(a):
    n = len(a)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] ^ a[i - 1]
    return max(dp)

def solve(n, a):
    return get_total_comfort(a)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))

