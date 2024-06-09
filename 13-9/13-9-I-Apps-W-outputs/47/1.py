
def solve(arr):
    n = len(arr)
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
    
    suffix_sum = [0] * (n + 1)
    for i in range(n, 0, -1):
        suffix_sum[i - 1] = suffix_sum[i] + arr[i - 1]
    
    total_sum = 0
    for i in range(n):
        total_sum += (prefix_sum[i] * (i + 1) + suffix_sum[i + 1] * (n - i)) % 1000000007
    
    return total_sum % 1000000007

