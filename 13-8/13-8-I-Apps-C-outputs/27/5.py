
import math

def get_common_factors(num1, num2):
    common_factors = []
    for i in range(2, int(math.sqrt(num1)) + 1):
        if num1 % i == 0 and num2 % i == 0:
            common_factors.append(i)
            if num1 // i != i and num2 // i != i:
                common_factors.append(num1 // i)
                common_factors.append(num2 // i)
    return common_factors

def count_ways(nums):
    n = len(nums)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][i] = 1
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            common_factors = get_common_factors(nums[i - 1], nums[j - 1])
            for k in range(1, n + 1):
                if k not in [i, j] and any(nums[k - 1] % f == 0 for f in common_factors):
                    dp[i][j] += dp[i][k] * dp[k][j]
    return dp[1][n] % 1000000007

if __name__ == '__main__':
    n = int(input())
    nums = [int(input()) for _ in range(n)]
    print(count_ways(nums))

