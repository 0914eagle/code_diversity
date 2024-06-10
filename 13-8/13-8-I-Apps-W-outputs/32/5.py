
def get_maximal_total_comfort(a):
    n = len(a)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(i, n + 1):
            if j == i:
                dp[i][j] = a[i]
            else:
                dp[i][j] = dp[i][j - 1] ^ a[j - 1]
    max_comfort = 0
    for i in range(n + 1):
        for j in range(i, n + 1):
            max_comfort = max(max_comfort, dp[i][j])
    return max_comfort

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(get_maximal_total_comfort(a))

if __name__ == '__main__':
    main()

