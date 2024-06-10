
def get_max_points(array):
    n = len(array)
    dp = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        dp[i] = max(dp[i + 1], array[i] + dp[i + 2])
    return dp[0]

def main():
    n = int(input())
    array = [int(x) for x in input().split()]
    print(get_max_points(array))

if __name__ == '__main__':
    main()

