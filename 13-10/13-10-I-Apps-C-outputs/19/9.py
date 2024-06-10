
def max_sum_after_swaps(arr, k):
    n = len(arr)
    if k >= n:
        return sum(arr)
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        dp[i][i] = arr[i]
    
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            dp[i][j] = max(dp[i][j-1], dp[i+1][j] + arr[i])
    
    for i in range(n):
        for j in range(i+1, n):
            dp[i][j] += arr[j]
    
    max_val = 0
    for i in range(n):
        for j in range(i+1, n):
            max_val = max(max_val, dp[i][j])
    
    return max_val

def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(max_sum_after_swaps(arr, k))

if __name__ == '__main__':
    main()

