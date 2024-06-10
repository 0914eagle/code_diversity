
def get_maximum_subset(x):
    n = len(x)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i):
            if x[i - 1] - x[j] == 2**dp[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp[n]

def get_subset(x, dp):
    n = len(x)
    subset = []
    i = n
    while i > 0:
        for j in range(i):
            if x[i - 1] - x[j] == 2**(dp[i] - 1):
                subset.append(x[j])
                i = j
                break
        if i == 0:
            break
    return subset[::-1]

if __name__ == '__main__':
    n = int(input())
    x = list(map(int, input().split()))
    dp = get_maximum_subset(x)
    subset = get_subset(x, dp)
    print(dp)
    print(*subset)

