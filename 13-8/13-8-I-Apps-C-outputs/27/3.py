
import math

def get_common_factors(x, y):
    common_factors = []
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0 and y % i == 0:
            common_factors.append(i)
            if x // i != i and y // i != i:
                common_factors.append(x // i)
                common_factors.append(y // i)
    return common_factors

def count_ways(nums):
    n = len(nums)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][i] = 1
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if get_common_factors(nums[i - 1], nums[j - 1]):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]
    return dp[n][n] % (10**9 + 7)

def main():
    nums = [int(input()) for _ in range(int(input()))]
    print(count_ways(nums))

if __name__ == '__main__':
    main()

