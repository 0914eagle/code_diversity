
def get_common_factors(x, y):
    common_factors = []
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0 and y % i == 0:
            common_factors.append(i)
    return common_factors

def get_number_of_ways(numbers):
    n = len(numbers)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                dp[i][j] = 1
            elif get_common_factors(numbers[i - 1], numbers[j - 1]):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][n]

def main():
    n = int(input())
    numbers = []
    for i in range(n):
        numbers.append(int(input()))
    print(get_number_of_ways(numbers) % 1000000007)

if __name__ == '__main__':
    main()

