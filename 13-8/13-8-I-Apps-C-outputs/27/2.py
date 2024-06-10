
def get_common_factors(num1, num2):
    common_factors = []
    for i in range(2, int(num1**0.5) + 1):
        if num1 % i == 0 and num2 % i == 0:
            common_factors.append(i)
            if num1 // i != i:
                common_factors.append(num1 // i)
            if num2 // i != i:
                common_factors.append(num2 // i)
    return sorted(set(common_factors))

def count_ways(nums):
    n = len(nums)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if get_common_factors(nums[i - 1], nums[j - 1]):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j - 1]
    return dp[n][n] % 1000000007

def main():
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(int(input()))
    print(count_ways(nums))

if __name__ == '__main__':
    main()

