
def get_occurrence(s, p):
    occurence = 0
    for i in range(len(s)):
        if s[i:i+len(p)] == p:
            occurence += 1
    return occurence

def solve(s, p):
    n = len(s)
    dp = [0] * (n+1)
    for i in range(n):
        dp[i+1] = max(dp[i], dp[i-len(p)] + 1)
    return dp

def main():
    s = input()
    p = input()
    dp = solve(s, p)
    print(*dp)

if __name__ == '__main__':
    main()

