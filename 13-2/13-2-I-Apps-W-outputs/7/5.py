
def get_maximum_circular_value(numbers):
    n = len(numbers)
    if n == 1:
        return numbers[0]
    
    # initialize dp array with all 0s
    dp = [0] * (n + 1)
    
    # calculate the maximum value for each subarray
    for i in range(1, n + 1):
        for j in range(0, n - i + 1):
            k = j + i - 1
            dp[j] = max(dp[j], dp[j + 1] + numbers[k] + numbers[j])
    
    return dp[0]

