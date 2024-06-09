
def f1(s, t):
    n = len(s)
    if n != len(t):
        return -1
    
    # Initialize the dp table with the number of moves needed for each prefix of s
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = i
    
    # Loop through the characters of s and t and calculate the minimum number of moves needed to transform s into t
    for i in range(n):
        for j in range(i, -1, -1):
            if s[i] == t[j]:
                dp[i + 1] = min(dp[i + 1], dp[j] + 1)
    
    return dp[n]

def f2(s, t):
    n = len(s)
    if n != len(t):
        return -1
    
    # Initialize the dp table with the number of moves needed for each suffix of s
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = i
    
    # Loop through the characters of s and t and calculate the minimum number of moves needed to transform s into t
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i] == t[j]:
                dp[i] = min(dp[i], dp[j + 1] + 1)
    
    return dp[0]

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        n = int(input())
        s = input()
        t = input()
        print(f1(s, t))
        print(f2(s, t))

