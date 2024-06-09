
def get_max_prettiness(a):
    n = len(a)
    if n == 1:
        return a[0]
    if n == 2:
        return a[0] + a[1]
    if n == 3:
        return max(a[0] + a[1], a[1] + a[2], a[0] + a[2])
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + a[i - 1], dp[i - 3] + a[i - 2] + a[i - 1])
    return dp[n]

def main():
    q = int(input())
    for _ in range(q):
        n = int(input())
        a = list(map(int, input().split()))
        print(get_max_prettiness(a))

if __name__ == '__main__':
    main()

