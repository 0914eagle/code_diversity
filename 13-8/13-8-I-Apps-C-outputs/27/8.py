
def get_common_factors(a, b):
    common_factors = []
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0 and b % i == 0:
            common_factors.append(i)
    return common_factors

def get_num_ways(nums):
    n = len(nums)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        dp[i][i] = 1
    for i in range(n - 1):
        for j in range(i + 1, n):
            if get_common_factors(nums[i], nums[j]):
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = dp[i][j - 1] + dp[i + 1][j]
    return dp[0][n - 1]

def main():
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(int(input()))
    print(get_num_ways(nums) % (10**9 + 7))

if __name__ == '__main__':
    main()

