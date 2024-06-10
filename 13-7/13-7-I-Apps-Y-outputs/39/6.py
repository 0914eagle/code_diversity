
def is_even(s):
    return s == s[::-1]

def longest_even(s):
    n = len(s)
    dp = [0] * (n + 1)
    for i in range(n):
        if is_even(s[:i + 1]):
            dp[i + 1] = dp[i] + 1
        else:
            dp[i + 1] = max(dp[i], dp[i - 1])
    return dp[n]

def main():
    s = input()
    print(longest_even(s))

if __name__ == '__main__':
    main()

