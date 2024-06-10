
def get_max_points(numbers):
    n = len(numbers)
    dp = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        dp[i] = max(dp[i + 1], dp[i + 2] + min(numbers[i], numbers[i + 1]))
    return dp[0]

def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    print(get_max_points(numbers))

if __name__ == '__main__':
    main()

