
def get_median(arr):
    arr.sort()
    if len(arr) % 2 == 0:
        return (arr[len(arr) // 2 - 1] + arr[len(arr) // 2]) / 2
    else:
        return arr[len(arr) // 2]

def is_scary(arr):
    return arr[0] == get_median(arr)

def count_scary_subarrays(arr):
    n = len(arr)
    dp = [0] * (n + 1)
    for i in range(n):
        dp[i + 1] = dp[i]
        if is_scary(arr[i:i + 1]):
            dp[i + 1] += 1
        for j in range(i):
            if is_scary(arr[j:i + 1]):
                dp[i + 1] += dp[j]
    return dp[n]

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(count_scary_subarrays(arr))

