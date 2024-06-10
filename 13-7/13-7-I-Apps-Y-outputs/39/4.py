
def is_even(s):
    return s == s[::-1]

def longest_even_substring(s):
    n = len(s)
    dp = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        if is_even(s[i:n]):
            dp[i] = 1
        else:
            dp[i] = max(dp[i + 1], dp[i + 2] + (s[i] != s[n - 1]))
    return n - dp[0]

def main():
    s = input()
    print(longest_even_substring(s))

if __name__ == '__main__':
    main()

