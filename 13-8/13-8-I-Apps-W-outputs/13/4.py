
def cut_string(s):
    n = len(s)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if s[i - 1] == '0':
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = dp[i - 1]
    for i in range(n - 1, -1, -1):
        if s[i] == '1':
            dp[i] = max(dp[i], dp[i + 1] + 1)
    return dp[0]

def get_cuts(s, k):
    n = len(s)
    cuts = []
    start = 0
    for i in range(n):
        if dp[i] == k:
            cuts.append(s[start:i])
            start = i
    cuts.append(s[start:])
    return cuts

def solve(s):
    k = cut_string(s)
    cuts = get_cuts(s, k)
    return k, cuts

if __name__ == '__main__':
    n = int(input())
    s = input()
    k, cuts = solve(s)
    print(k)
    print(' '.join(cuts))

