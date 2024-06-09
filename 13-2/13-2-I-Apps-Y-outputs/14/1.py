
def get_max_divisible_numbers(s):
    n = len(s)
    dp = [0] * (n + 1)
    for i in range(n):
        if s[i] == '3':
            dp[i + 1] = 1
        elif s[i] == '0':
            if i + 1 < n and s[i + 1] == '3':
                dp[i + 2] = 1
        else:
            if i + 1 < n and s[i + 1] == '0':
                dp[i + 2] = 1
            if i - 1 >= 0 and s[i - 1] == '3':
                dp[i + 1] = 1
    return dp[n]

def main():
    s = input()
    print(get_max_divisible_numbers(s))

if __name__ == '__main__':
    main()

