
def get_max_sum(numbers):
    n = len(numbers)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + numbers[i - 1])
    return dp[n]

def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    print(get_max_sum(numbers))

if __name__ == '__main__':
    main()

