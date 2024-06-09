
def get_min_cost(s, k):
    n = len(s)
    dp = [[0] * (k+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, k+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = max(dp[i-1][j-1] + 1, dp[i-1][j])
    return dp[n][k]

def get_subsequences(s):
    subsequences = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            subsequences.append(s[i:j])
    return subsequences

def solve(s, k):
    subsequences = get_subsequences(s)
    min_cost = get_min_cost(s, k)
    if min_cost == -1:
        return -1
    else:
        return min_cost

if __name__ == '__main__':
    s = input()
    k = int(input())
    print(solve(s, k))

