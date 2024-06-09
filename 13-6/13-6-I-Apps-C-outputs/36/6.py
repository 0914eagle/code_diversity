
def longest_non_decreasing_sequence(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] >= arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

def main():
    n, T = map(int, input().split())
    arr = list(map(int, input().split()))
    print(longest_non_decreasing_sequence(arr))

if __name__ == '__main__':
    main()

