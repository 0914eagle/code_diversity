
def get_max_points(numbers):
    n = len(numbers)
    dp = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        dp[i] = max(numbers[i], dp[i + 1])
    for i in range(1, n):
        dp[i] = max(dp[i - 1], dp[i])
    return sum(dp)

def main():
    n = int(input())
    numbers = [int(x) for x in input().split()]
    print(get_max_points(numbers))

if __name__ == '__main__':
    main()

