
def get_maximum_tastiness(n, k, a, b, t, u):
    # Initialize the dp table
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Base case: no scoops
    for i in range(k + 1):
        dp[0][i] = 0
    
    # Populate the dp table
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = max(dp[i - 1][j - 1] + t[j - 1], dp[i - 1][j] + t[j - 1] + u[j - 1])
    
    # Find the maximum tastiness per gold coin ratio
    max_ratio = 0
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if dp[i][j] > 0:
                ratio = dp[i][j] / (a * i + b)
                if ratio > max_ratio:
                    max_ratio = ratio
    
    return max_ratio

def main():
    n, k, a, b = map(int, input().split())
    t = list(map(int, input().split()))
    u = []
    for i in range(k):
        u.append(list(map(int, input().split())))
    
    print(get_maximum_tastiness(n, k, a, b, t, u))

if __name__ == '__main__':
    main()

