
def get_max_comfort(cities):
    n = len(cities)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                dp[i][j] = 0
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 1] + cities[j - 1] ^ cities[i - 1])
    return dp[n][n]

def main():
    n = int(input())
    cities = [int(x) for x in input().split()]
    print(get_max_comfort(cities))

if __name__ == '__main__':
    main()

