
def f1(n, m):
    # Calculate the number of subsequences of length n for each element in the range [1, m]
    dp = [0] * (m + 1)
    dp[0] = 1
    for i in range(1, m + 1):
        dp[i] = (dp[i - 1] + dp[i - 1]) % (10**9 + 7)
    
    # Calculate the sum of the number of subsequences of length n for all elements in the range [1, m]
    sum = 0
    for i in range(n):
        sum = (sum + dp[i]) % (10**9 + 7)
    
    return sum

def f2(n, m):
    # Calculate the number of subsequences of length n for each element in the range [1, m]
    dp = [0] * (m + 1)
    dp[0] = 1
    for i in range(1, m + 1):
        dp[i] = (dp[i - 1] + dp[i - 1]) % (10**9 + 7)
    
    # Calculate the sum of the number of subsequences of length n for all elements in the range [1, m]
    sum = 0
    for i in range(n):
        sum = (sum + dp[i]) % (10**9 + 7)
    
    return sum

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(f1(n, m))
    print(f2(n, m))

