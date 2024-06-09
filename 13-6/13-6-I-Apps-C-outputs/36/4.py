
def get_longest_non_decreasing_sequence(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    return max(dp)

def solve(arr):
    n, T = map(int, input().split())
    arr = [int(x) for x in input().split()]
    return get_longest_non_decreasing_sequence(arr * T)

if __name__ == '__main__':
    print(solve([int(x) for x in input().split()]))

