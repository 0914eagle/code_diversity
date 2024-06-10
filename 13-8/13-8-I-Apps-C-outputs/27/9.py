
def get_common_factors(num1, num2):
    common_factors = []
    for i in range(2, int(num1**0.5) + 1):
        if num1 % i == 0 and num2 % i == 0:
            common_factors.append(i)
            if num1 // i != i:
                common_factors.append(num1 // i)
            if num2 // i != i:
                common_factors.append(num2 // i)
    return set(common_factors)

def get_number_of_ways(nums):
    n = len(nums)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                dp[i][j] = 1
            else:
                common_factors = get_common_factors(nums[i - 1], nums[j - 1])
                dp[i][j] = sum(dp[i - 1][k] * dp[k + 1][j] for k in range(i, j) if k not in common_factors)
    return dp[1][n] % 1000000007

def main():
    nums = [int(input()) for _ in range(int(input()))]
    print(get_number_of_ways(nums))

if __name__ == '__main__':
    main()

