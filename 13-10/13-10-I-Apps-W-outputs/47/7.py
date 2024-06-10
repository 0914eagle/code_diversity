
def get_beauty(arr, k):
    n = len(arr)
    beauty = 0
    for i in range(n - k + 1):
        for j in range(i + 1, n):
            beauty += abs(arr[i] - arr[j])
    return beauty % 998244353

def get_sum_of_beauty(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = get_beauty(arr[:i], k)
    return sum(dp) % 998244353

def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(get_sum_of_beauty(arr, k))

if __name__ == '__main__':
    main()

