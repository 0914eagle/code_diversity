
import math

def get_coprime_subsequences(arr):
    n = len(arr)
    dp = [1] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, i):
            if arr[i - 1] % arr[j - 1] == 0:
                dp[i] = (dp[i] - dp[j] + 1000000007) % 1000000007
    return dp[n]

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_coprime_subsequences(arr))

if __name__ == '__main__':
    main()

